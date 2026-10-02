/* Original fixed-grid pixel mascot, enlarged without smoothing. */
'use strict';
window.foamPandaArt = (face=false) => `<canvas class="panda-art panda-pixel-art" width="128" height="${face?128:144}" ${face?'data-face-only="true"':''} aria-hidden="true"></canvas>`;
