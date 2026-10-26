# Sabino fonts

`sabino-fonts.js` is a Lovelace module that loads the Sabino theme's fonts for the
whole page with no network: Hanken Grotesk 400–700, JetBrains Mono 400–500,
Newsreader 400–600 and Newsreader Italic 400. Installing it is covered in the main
[README](../README.md#4-add-the-fonts).

## Why a module and not the theme

A Home Assistant theme can only carry CSS through card-mod, which puts it inside a
shadow root. Chromium (Chrome, Edge, the Android app) ignores `@font-face` and
`@import` there, so fonts loaded by the theme never showed in those browsers. WebKit
(Safari, the iOS app) accepts them, but a Google Fonts `@import` often failed when
the app opened while the network was still switching, and WebKit doesn't retry a
failed font until the page reloads.

A module runs at page level and adds the fonts with the `FontFace` API, which every
browser applies inside every card. The font files are embedded, so nothing has to
download. It also re-checks the fonts when the app comes back to the foreground.

## Files

- `*.woff2`: latin subsets of the Google Fonts releases, limited to the weights the
  theme uses (fontTools `varLib.instancer` and `pyftsubset`). Newsreader keeps its
  optical-size axis.
- `licenses/`: the SIL Open Font License for each family. The fonts are free to use
  and redistribute under it.
- `build.py`: writes `sabino-fonts.js` from the four files. Bump `VERSION` first.
- `sabino-fonts.js`: the built module, also attached to each GitHub release.
