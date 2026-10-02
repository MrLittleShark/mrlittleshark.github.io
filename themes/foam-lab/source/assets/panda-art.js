/* Original fixed-grid pixel mascot, enlarged without smoothing. */
'use strict';
window.foamPandaArt = (face=false) => `<canvas class="panda-art panda-pixel-art" width="64" height="${face?64:72}" ${face?'data-face-only="true"':''} aria-hidden="true"></canvas>`;
