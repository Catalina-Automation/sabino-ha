<div align="center">

# Sabino for Home Assistant

**A quiet Sonoran theme for Home Assistant**, by [Catalina Automation](https://usecatalina.ai).
Sabino Day in canyon sand, Sabino Night in canyon green, switching with your device.

[![HACS Custom](https://img.shields.io/badge/HACS-Custom-41BDF5?style=flat-square)](https://hacs.xyz/docs/faq/custom_repositories/)
[![Release](https://img.shields.io/github/v/release/Catalina-Automation/sabino-ha?style=flat-square&label=release)](https://github.com/Catalina-Automation/sabino-ha/releases)
[![Stars](https://img.shields.io/github/stars/Catalina-Automation/sabino-ha?style=flat-square)](https://github.com/Catalina-Automation/sabino-ha/stargazers)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2026.10-18BCF2?style=flat-square)](https://www.home-assistant.io/)
[![License](https://img.shields.io/github/license/Catalina-Automation/sabino-ha?style=flat-square)](https://github.com/Catalina-Automation/sabino-ha/blob/main/LICENSE)

[Install](#install) · [Screenshots](#screenshots) · [Fonts and cards](#fonts-and-cards) · [Sabino for terminals and editors](https://github.com/Catalina-Automation/sabino-theme)

<img src="https://raw.githubusercontent.com/Catalina-Automation/sabino-ha/main/images/day.webp" alt="Sabino Day on a Home Assistant dashboard" width="100%">

</div>

## Why Sabino?

Home Assistant's default colors are bright and generic: stock red, green, and yellow
for every state, on every card. Sabino replaces all of them with one restrained
palette. Green means it worked, clay means it stopped, gold means look at this.
Nothing else gets to be loud.

## Features

| | |
|---|---|
| **Day and Night** | One theme with light and dark modes. Set Home Assistant to Auto and it follows your device. |
| **Every color** | Overrides every color variable Home Assistant's frontend defines, as of 2026.10, so no stock color shows through. |
| **State colors** | Gauges, tiles, badges, alerts, and climate modes draw from the palette instead of Home Assistant's defaults. |
| **Typography** | Newsreader for headings and big numbers, Hanken Grotesk for interface text, JetBrains Mono for times and code. |
| **Bubble Card** | Radii, surfaces, shadows, accent, and climate colors cascade to every Bubble Card with no extra setup. |
| **Design tokens** | The raw palette (`--clay-400`, `--sage-500`, `--sand-200`, …) and aliases such as `--brand` are CSS variables your own cards can use. |

## Screenshots

<table>
  <tr>
    <td width="50%"><img src="https://raw.githubusercontent.com/Catalina-Automation/sabino-ha/main/images/day.webp" alt="Sabino Day"><br><sub><b>Sabino Day</b> · canyon sand surfaces, clay and gold accents</sub></td>
    <td width="50%"><img src="https://raw.githubusercontent.com/Catalina-Automation/sabino-ha/main/images/night.webp" alt="Sabino Night"><br><sub><b>Sabino Night</b> · canyon green surfaces, sand text</sub></td>
  </tr>
</table>

## Install

### 1. Download with HACS

[![Open your Home Assistant instance and open this repository in HACS.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Catalina-Automation&repository=sabino-ha&category=theme)

Or by hand:

1. Open **HACS** in Home Assistant.
2. Open the menu (⋮, top right) and choose **Custom repositories**.
3. Add `https://github.com/Catalina-Automation/sabino-ha` with type **Theme**.
4. Search for **Sabino**, open it and choose **Download**.

<details>
<summary>Manual download (without HACS)</summary>

Copy [`themes/sabino.yaml`](themes/sabino.yaml) into the `themes/` folder of your
Home Assistant config.

</details>

### 2. Load themes

Home Assistant only reads the `themes/` folder if `configuration.yaml` says so. If
yours doesn't already, add this and restart:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

> 💡 Already have a `frontend:` section? Add `themes:` to it instead of adding a second one.

Otherwise, run the `frontend.reload_themes` action to pick up the new theme without
restarting.

### 3. Choose Sabino

Open your **Profile**, set **Theme** to **Sabino**, and leave the mode on **Auto** to
follow your device. Choose Light or Dark to pin one.

To make Sabino the default for everyone, call `frontend.set_theme` with
`name: Sabino` twice, once with `mode: light` and once with `mode: dark`.

## Fonts and cards

- **Fonts** load from Google Fonts through
  [card-mod](https://github.com/thomasloven/lovelace-card-mod). Without card-mod, or
  without internet access, the colors still apply and text uses Home Assistant's
  default font.
- **[Bubble Card](https://github.com/Clooos/Bubble-Card)** is optional. If you use it,
  it picks up the theme on its own.

## License

MIT. See [LICENSE](LICENSE).
