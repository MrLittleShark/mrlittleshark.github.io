#!/usr/bin/env python3
"""Check the checked-in course assets without contacting or changing the CMS.

Run from any directory with Python 3.9+: python tools/check-course-assets.py
The only output file is .openfoam-work/course-refinement/asset-integrity.json.
Exit status is 0 on success and 1 when any integrity check fails.
"""

from __future__ import annotations

import hashlib
import json
import re
import struct
import sys
import zipfile
import zlib
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source-openfoam"
CONTENT = ROOT / "tools/content"
REPORT = ROOT / ".openfoam-work/course-refinement/asset-integrity.json"
TOPICS = ("turbulence", "multiphase", "meshing", "dynamic-mesh")
EXPECTED_LESSONS = 46
EXPECTED_FIGURES = 37
SHA256 = re.compile(r"[0-9a-fA-F]{64}\Z")


class Images(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.urls = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "img":
            self.urls.extend(value for key, value in attrs if key == "src" and value)


class Check:
    def __init__(self):
        self.errors = []
        self.files = {}
        self.origin = "https://mrlittleshark.github.io"
        config = ROOT / "_config.yml"
        if config.is_file():
            match = re.search(r"^url:\s*([^\s#]+)", config.read_text(encoding="utf-8-sig"), re.M)
            if match:
                self.origin = match.group(1).strip("\"'").rstrip("/")
        self.report = {
            "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "scope": "Local CMS source records and asset files; no database or network access.",
            "site_origin": self.origin,
            "content_records": 0,
            "lessons": 0,
            "lessons_with_downloads": 0,
            "download_references": 0,
            "unique_download_files": 0,
            "download_bytes": 0,
            "zip_archives": 0,
            "zip_entries_crc_checked": 0,
            "topics": {},
            "wolf_figures": 0,
            "wolf_figures_referenced": 0,
            "wolf_body_references": 0,
            "wolf_image_bytes": 0,
        }

    def error(self, context, message):
        self.errors.append({"context": context, "message": message})

    def load(self, path):
        try:
            data = json.loads(path.read_text(encoding="utf-8-sig"))
        except (OSError, ValueError) as exc:
            self.error(str(path.relative_to(ROOT)), str(exc))
            return []
        if not isinstance(data, list) or any(not isinstance(item, dict) for item in data):
            self.error(str(path.relative_to(ROOT)), "Expected an array of objects")
            return []
        return data

    def local_file(self, url, prefix, context):
        """Resolve only same-origin canonical URLs contained in the source tree."""
        if not isinstance(url, str) or not url or any(c.isspace() for c in url):
            self.error(context, "Missing or invalid asset URL")
            return None
        try:
            parsed = urlsplit(url)
            origin = urlsplit(self.origin)
            if parsed.scheme or parsed.netloc:
                if (parsed.scheme, parsed.hostname, parsed.port) != (origin.scheme, origin.hostname, origin.port):
                    raise ValueError("Asset URL must have the configured site origin")
                if parsed.username or parsed.password:
                    raise ValueError("Asset URL cannot contain credentials")
            elif not url.startswith("/") or url.startswith("//"):
                raise ValueError("Asset URL must be root-relative or use the configured site origin")
            if parsed.query or parsed.fragment:
                raise ValueError("Asset URL must not contain a query or fragment")
            path = unquote(parsed.path, errors="strict")
            if "%" in path or "\\" in path or "\x00" in path:
                raise ValueError("Asset path contains non-canonical escaping or a backslash")
            if not path.startswith(prefix) or any(part in (".", "..", "") for part in path[1:].split("/")):
                raise ValueError(f"Asset must be a canonical path under {prefix}")
            target = (SOURCE / path.lstrip("/")).resolve()
            target.relative_to(SOURCE.resolve())
            if not target.is_file():
                raise ValueError(f"Asset file is missing: {path}")
            return target
        except (ValueError, UnicodeError, OSError) as exc:
            self.error(context, str(exc))
            return None

    def fingerprint(self, path, context):
        if path not in self.files:
            try:
                digest = hashlib.sha256()
                with path.open("rb") as stream:
                    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                        digest.update(chunk)
                self.files[path] = {"size": path.stat().st_size, "sha256": digest.hexdigest()}
            except OSError as exc:
                self.error(context, f"Cannot read asset: {exc}")
                return None
        return self.files[path]

    def declared_hash(self, actual, expected, context):
        if not isinstance(expected, str) or not SHA256.fullmatch(expected):
            self.error(context, "Missing or malformed SHA-256 declaration")
        elif actual != expected.lower():
            self.error(context, f"SHA-256 mismatch: expected {expected.lower()}, got {actual}")

    def downloads(self, lessons):
        seen = set()
        for lesson in lessons:
            slug = lesson["slug"]
            downloads = self.metadata(lesson).get("downloads")
            if not isinstance(downloads, list) or not downloads:
                self.error(slug, "Lesson must declare a nonempty metadata.downloads array")
                continue
            self.report["lessons_with_downloads"] += 1
            lesson_urls = set()
            for index, item in enumerate(downloads):
                context = f"{slug}:downloads[{index}]"
                self.report["download_references"] += 1
                if not isinstance(item, dict):
                    self.error(context, "Download must be an object")
                    continue
                path = self.local_file(item.get("url"), "/downloads/", context)
                if path is None:
                    continue
                if path in lesson_urls:
                    self.error(context, "Duplicate download within the lesson")
                lesson_urls.add(path)
                actual = self.fingerprint(path, context)
                if actual is None:
                    continue
                declared_size = item.get("size_bytes")
                if type(declared_size) is not int or declared_size <= 0:
                    self.error(context, "size_bytes must be a positive integer")
                elif actual["size"] != declared_size:
                    self.error(context, f"Size mismatch: expected {declared_size}, got {actual['size']}")
                self.declared_hash(actual["sha256"], item.get("sha256"), context)
                if path in seen:
                    continue
                seen.add(path)
                self.report["download_bytes"] += actual["size"]
                if path.suffix.lower() == ".zip":
                    self.report["zip_archives"] += 1
                    try:
                        with zipfile.ZipFile(path) as archive:
                            bad_member = archive.testzip()
                            if bad_member:
                                self.error(context, f"ZIP CRC failed: {bad_member}")
                            else:
                                self.report["zip_entries_crc_checked"] += len(archive.infolist())
                    except (OSError, ValueError, RuntimeError, NotImplementedError, zipfile.BadZipFile, zlib.error, EOFError) as exc:
                        self.error(context, f"ZIP integrity check failed: {exc}")
        self.report["unique_download_files"] = len(seen)

    def metadata(self, record):
        metadata = record.get("metadata", {})
        if not isinstance(metadata, dict):
            self.error(record.get("slug", "unknown record"), "metadata must be an object")
            return {}
        return metadata

    def topics(self, records, lessons):
        modules = {}
        for record in records:
            key = self.metadata(record).get("topic_key")
            if key is None:
                continue
            slug = record["slug"]
            if key not in TOPICS:
                self.error(slug, f"Unknown topic_key: {key!r}")
                continue
            if key in modules:
                self.error(slug, f"Duplicate topic_key: {key}")
            modules[key] = record
            if record.get("kind") != "module" or record.get("status") != "published":
                self.error(slug, "Topic must be a published module")
            if slug != f"topic-{key}":
                self.error(slug, f"Topic slug must be topic-{key}")
            if self.metadata(record).get("canonical_path") != f"/topics/{key}/":
                self.error(slug, "Topic canonical_path does not match its key")
            if not (SOURCE / "topics" / key / "index.md").is_file():
                self.error(slug, "Static topic route is missing")
        counts = Counter()
        for lesson in lessons:
            slug = lesson["slug"]
            keys = self.metadata(lesson).get("topics", [])
            if not isinstance(keys, list):
                self.error(slug, "metadata.topics must be an array (it may be empty)")
                continue
            seen = set()
            for key in keys:
                if not isinstance(key, str) or key not in TOPICS:
                    self.error(slug, f"Unknown lesson topic: {key!r}")
                    continue
                if key in seen:
                    self.error(slug, f"Duplicate lesson topic: {key}")
                    continue
                seen.add(key)
                if key not in modules:
                    self.error(slug, f"Lesson links to a missing topic module: {key}")
                if lesson.get("status") == "published":
                    counts[key] += 1
        for key in TOPICS:
            if key not in modules:
                self.error("topics", f"Missing topic module: {key}")
            if not counts[key]:
                self.error("topics", f"No published lesson is associated with {key}")
        self.report["topics"] = {key: counts[key] for key in TOPICS}

    def figures(self, records, lessons):
        figures = self.load(CONTENT / "wolf-figures.json")
        self.report["wolf_figures"] = len(figures)
        if len(figures) != EXPECTED_FIGURES:
            self.error("wolf-figures.json", f"Expected {EXPECTED_FIGURES} figures, found {len(figures)}")
        lesson_slugs = {record["slug"] for record in lessons}
        by_id, by_path = {}, {}
        for figure in figures:
            ident = figure.get("id")
            context = str(ident or "wolf-figures.json")
            if not isinstance(ident, str) or not ident:
                self.error(context, "Missing figure id")
                continue
            if ident in by_id:
                self.error(context, "Duplicate figure id")
            by_id[ident] = figure
            path = self.local_file(figure.get("file"), "/assets/wolf/", context)
            if path is not None:
                if path in by_path:
                    self.error(context, "Two manifest entries refer to the same image")
                by_path[path] = ident
                actual = self.fingerprint(path, context)
                if actual:
                    self.report["wolf_image_bytes"] += actual["size"]
                    self.declared_hash(actual["sha256"], figure.get("sha256"), context)
                try:
                    with path.open("rb") as stream:
                        header = stream.read(24)
                    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
                        raise ValueError("Not a PNG with a valid IHDR header")
                    width, height = struct.unpack(">II", header[16:24])
                    resolution = figure.get("resolution", {})
                    if not isinstance(resolution, dict) or (width, height) != (resolution.get("width"), resolution.get("height")):
                        raise ValueError(f"PNG dimensions do not match manifest: {width} x {height}")
                    if width <= 0 or height <= 0:
                        raise ValueError("PNG dimensions must be positive")
                except (OSError, ValueError, struct.error) as exc:
                    self.error(context, str(exc))
            related = figure.get("related_slugs")
            if not isinstance(related, list) or not related:
                self.error(context, "related_slugs must identify at least one lesson")
            else:
                for slug in related:
                    if not isinstance(slug, str) or slug not in lesson_slugs:
                        self.error(context, f"related_slugs contains an unknown lesson: {slug!r}")

        referenced = set()
        for record in records:
            body = record.get("body", "")
            if not isinstance(body, str):
                self.error(record["slug"], "body must be a string")
                continue
            parser = Images()
            parser.feed(body)
            urls = parser.urls + re.findall(r"!\[[^\]]*\]\(\s*<?([^\s)>]+)>?(?:\s+[^)]*)?\)", body)
            present = set()
            for url in urls:
                if "/assets/wolf/" not in url:
                    continue
                path = self.local_file(url, "/assets/wolf/", record["slug"])
                if path is None:
                    continue
                ident = by_path.get(path)
                if ident is None:
                    self.error(record["slug"], f"Wolf body image is absent from manifest: {url}")
                    continue
                present.add(ident)
                if record.get("status") == "published":
                    referenced.add(ident)
                    self.report["wolf_body_references"] += 1
            declared = self.metadata(record).get("wolf_figures", [])
            if not isinstance(declared, list):
                self.error(record["slug"], "metadata.wolf_figures must be an array")
            else:
                for ident in declared:
                    if not isinstance(ident, str) or ident not in by_id:
                        self.error(record["slug"], f"Unknown declared Wolf figure: {ident!r}")
                    elif ident not in present:
                        self.error(record["slug"], f"Declared Wolf figure is absent from this body: {ident}")
        for ident in sorted(by_id.keys() - referenced):
            self.error(ident, "Figure is not referenced by an image in any published content body")
        self.report["wolf_figures_referenced"] = len(referenced)

    def run(self):
        records, slugs = [], set()
        for path in sorted(CONTENT.glob("*content.json")):
            for record in self.load(path):
                slug = record.get("slug")
                if not isinstance(slug, str) or not slug:
                    self.error(path.name, "Record has no valid slug")
                    continue
                if slug in slugs:
                    self.error(path.name, f"Duplicate content slug: {slug}")
                slugs.add(slug)
                records.append(record)
        self.report["content_records"] = len(records)
        lessons = [record for record in records if record.get("kind") == "lesson"]
        self.report["lessons"] = len(lessons)
        if len(lessons) != EXPECTED_LESSONS:
            self.error("lessons", f"Expected {EXPECTED_LESSONS} lessons, found {len(lessons)}")
        self.downloads(lessons)
        self.topics(records, lessons)
        self.figures(records, lessons)
        self.report["ok"] = not self.errors
        self.report["errors"] = self.errors
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(json.dumps(self.report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(self.report, ensure_ascii=False, separators=(",", ":")))
        return 0 if not self.errors else 1


if __name__ == "__main__":
    sys.exit(Check().run())
