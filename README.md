# Sabino for Home Assistant

A quiet Sonoran theme for Home Assistant dashboards, by [Catalina Automation](https://usecatalina.ai).
One theme, two modes: **Sabino Day** (cream) and **Sabino Night** (canyon green). Home
Assistant moves between them with your device's light and dark setting.

![Sabino Day](https://raw.githubusercontent.com/Catalina-Automation/sabino-ha/main/images/day.webp)

![Sabino Night](https://raw.githubusercontent.com/Catalina-Automation/sabino-ha/main/images/night.webp)

The same palette is available for terminals and editors in
[sabino-theme](https://github.com/Catalina-Automation/sabino-theme).

## Install

### HACS

1. HACS › ⋮ › Custom repositories. Add `https://github.com/Catalina-Automation/sabino-ha`
   with type **Theme**.
2. Search for Sabino and download it.
3. Restart Home Assistant, or run the `frontend.reload_themes` action.

### Manually

Copy `themes/sabino.yaml` into the `themes/` folder of your Home Assistant config,
then reload themes.

Either way, Home Assistant has to be loading themes from that folder. If it isn't
already, add this to `configuration.yaml` and restart:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

## Use

Profile › Theme › **Sabino**, with the mode set to Auto to follow the device. Set
Light or Dark to pin one. To make it the default for every user, call
`frontend.set_theme` with `name: Sabino` twice, once with `mode: light` and once
with `mode: dark`.

## Fonts and cards

- **Fonts** (Newsreader, Hanken Grotesk, JetBrains Mono) load through
  [card-mod](https://github.com/thomasloven/lovelace-card-mod). Without card-mod the
  colors still apply and text uses Home Assistant's default font.
- **[Bubble Card](https://github.com/Clooos/Bubble-Card)** picks up the theme's
  radii, surfaces, and accent with no extra setup.
- The raw palette (`--clay-400`, `--sage-500`, `--sand-200`, …) and aliases such as
  `--brand` are exposed as CSS variables, so card `styles:` and card-mod blocks can
  use them directly.

## License

MIT. See [LICENSE](LICENSE).
