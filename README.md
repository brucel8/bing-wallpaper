# Bing Daily Wallpaper

Every Sunday, GitHub Actions downloads the past week's Bing daily wallpapers (4K UHD, falling back to 1080p) into this repository. No local machine needs to stay on.

- All images live in `pics/`, named `YYYYMMDD_title.jpg`
- `latest.jpg` always points to the newest one — shown below

![Latest wallpaper](latest.jpg)

## Gallery (click a thumbnail for the full image)

<!-- GALLERY-START -->

_No images yet_

<!-- GALLERY-END -->

## Manual actions

- Run it now: Actions tab → Bing Daily Wallpaper → Run workflow
- Run the script locally: `python3 bing_wallpaper.py 8 -o pics` (last 8 days; the number can be 1–8)

## Notes

- Schedule: Sundays 00:15 UTC. Each run fetches the last 8 days (the past week plus one spare day in case a run is missed; images already present are skipped). Scheduled runs may start some minutes late when GitHub is busy — that is normal.
- A UHD image is about 1–3 MB, so the repository grows by roughly 0.5–1 GB per year.
