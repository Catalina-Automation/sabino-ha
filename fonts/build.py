#!/usr/bin/env python3
"""Build sabino-fonts.js: one Lovelace module that registers the Sabino fonts
for the whole page, with the woff2 files embedded, so no network is needed.

    python3 fonts/build.py

Bump VERSION on every change, so the README's resource URL (?v=VERSION) also
changes and browsers don't keep a stale copy.
"""
import base64
import pathlib

HERE = pathlib.Path(__file__).parent
VERSION = "1.1.0"

# Same latin range Google Fonts serves; other scripts fall back to system fonts.
UNICODE_RANGE = (
    "U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, "
    "U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD"
)

# (file, family, style, weights)
FACES = [
    ("hanken-grotesk-latin-400-700.woff2", "Hanken Grotesk", "normal", ["400", "500", "600", "700"]),
    ("jetbrains-mono-latin-400-500.woff2", "JetBrains Mono", "normal", ["400", "500"]),
    ("newsreader-latin-400-600.woff2", "Newsreader", "normal", ["400", "500", "600"]),
    ("newsreader-italic-latin-400.woff2", "Newsreader", "italic", ["400"]),
]

TEMPLATE = r"""/*
 * sabino-fonts v%(ver)s - fonts for the Sabino Home Assistant theme
 * https://github.com/Catalina-Automation/sabino-ha
 *
 * Registers Hanken Grotesk, JetBrains Mono and Newsreader for the whole page
 * (every card's shadow root included) from embedded files, with no network.
 *
 * The embedded fonts are latin subsets, licensed under the SIL Open Font License 1.1
 * (fonts/licenses/ in the repository):
 *   Copyright 2021 The Hanken Grotesk Project Authors (https://github.com/marcologous/hanken-grotesk)
 *   Copyright 2020 The JetBrains Mono Project Authors (https://github.com/JetBrains/JetBrainsMono)
 *   Copyright 2020 The Newsreader Project Authors (http://github.com/productiontype/Newsreader)
 */
(() => {
  const W = window, D = document, KEY = "__sabinoFonts", ID = "sabino-fonts";
  const R = (W[KEY] = W[KEY] || { version: "%(ver)s", bundles: {} });
  if (R.bundles[ID] || !D.fonts || typeof FontFace === "undefined") return;
  const UR = "%(ur)s";
  const SPECS = %(specs)s;
  const faces = [];
  for (const [b64, family, style, weights] of SPECS) {
    const bin = Uint8Array.from(atob(b64), (c) => c.charCodeAt(0));
    for (const weight of weights) {
      faces.push(new FontFace(family, bin.slice().buffer, { style, weight, display: "swap", unicodeRange: UR }));
    }
  }
  R.bundles[ID] = faces;
  let nudged = 0;
  const nudge = () => {
    // Re-measure anything that sized itself with fallback metrics.
    clearTimeout(nudged);
    nudged = setTimeout(() => requestAnimationFrame(() => W.dispatchEvent(new Event("resize"))), 50);
  };
  const ensure = () => {
    let added = false;
    for (const f of faces) {
      if (!D.fonts.has(f)) { D.fonts.add(f); added = true; }
      if (f.status === "unloaded" || f.status === "error") f.load().catch(() => {});
    }
    if (added) Promise.all(faces.map((f) => f.loaded.catch(() => null))).then(nudge);
  };
  ensure();
  // iOS app resume and back-forward cache restore: make sure the faces are still registered.
  W.addEventListener("pageshow", ensure);
  D.addEventListener("visibilitychange", () => { if (D.visibilityState === "visible") ensure(); });
})();
"""

specs = []
for fn, family, style, weights in FACES:
    b64 = base64.b64encode((HERE / fn).read_bytes()).decode()
    specs.append('["%s", "%s", "%s", [%s]]' % (b64, family, style, ",".join('"%s"' % w for w in weights)))
js = TEMPLATE % dict(ver=VERSION, ur=UNICODE_RANGE, specs="[\n    " + ",\n    ".join(specs) + "\n  ]")
(HERE / "sabino-fonts.js").write_text(js)
print("sabino-fonts.js", len(js.encode()), "bytes")
