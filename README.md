# Bing Daily Wallpaper

Every Sunday, GitHub Actions downloads the past week's Bing daily wallpapers (4K UHD, falling back to 1080p) into this repository. No local machine needs to stay on.

- All images live in `pics/`, named `YYYYMMDD_title.jpg`
- `latest.jpg` always points to the newest one — shown below

![Latest wallpaper](latest.jpg)

## Gallery (click a thumbnail for the full image)

<!-- GALLERY-START -->

### November 2026 (latest month)

| | | | |
|---|---|---|---|
| [![2026-11-13](thumbs/20261113_%E5%94%AF%E6%9C%89%E5%90%91%E4%B8%8A%E5%8F%91%E5%B1%95.jpg)](pics/20261113_%E5%94%AF%E6%9C%89%E5%90%91%E4%B8%8A%E5%8F%91%E5%B1%95.jpg)<br>2026-11-13 | [![2026-11-12](thumbs/20261112_%E5%86%B0%E4%B8%8B%E7%A7%98%E5%A2%83.jpg)](pics/20261112_%E5%86%B0%E4%B8%8B%E7%A7%98%E5%A2%83.jpg)<br>2026-11-12 | [![2026-11-11](thumbs/20261111_%E6%B2%A1%E6%9C%89%E5%BB%BA%E7%AD%91%E5%B8%88%E7%9A%84%E5%BB%BA%E7%AD%91%E6%9D%B0%E4%BD%9C.jpg)](pics/20261111_%E6%B2%A1%E6%9C%89%E5%BB%BA%E7%AD%91%E5%B8%88%E7%9A%84%E5%BB%BA%E7%AD%91%E6%9D%B0%E4%BD%9C.jpg)<br>2026-11-11 | [![2026-11-10](thumbs/20261110_%E5%A5%87%E5%A6%99%E7%BA%B7%E5%91%88%E7%9A%84%E6%A3%AE%E6%9E%97.jpg)](pics/20261110_%E5%A5%87%E5%A6%99%E7%BA%B7%E5%91%88%E7%9A%84%E6%A3%AE%E6%9E%97.jpg)<br>2026-11-10 |
| [![2026-11-09](thumbs/20261109_%E6%83%AC%E6%84%8F%E6%94%BE%E6%9D%BE%EF%BC%8C%E5%B0%BD%E4%BA%AB%E6%B5%B7%E5%B2%9B%E6%97%B6%E5%85%89.jpg)](pics/20261109_%E6%83%AC%E6%84%8F%E6%94%BE%E6%9D%BE%EF%BC%8C%E5%B0%BD%E4%BA%AB%E6%B5%B7%E5%B2%9B%E6%97%B6%E5%85%89.jpg)<br>2026-11-09 | [![2026-11-08](thumbs/20261108_%E8%89%BA%E6%9C%AF%E4%B8%8E%E9%9F%B5%E5%BE%8B%E4%BA%A4%E6%B1%87%E4%B9%8B%E5%9C%B0.jpg)](pics/20261108_%E8%89%BA%E6%9C%AF%E4%B8%8E%E9%9F%B5%E5%BE%8B%E4%BA%A4%E6%B1%87%E4%B9%8B%E5%9C%B0.jpg)<br>2026-11-08 | [![2026-11-07](thumbs/20261107_%E5%85%89%E8%8A%92%E5%9B%9B%E5%B0%84%E7%9A%84%E8%8A%82%E6%97%A5.jpg)](pics/20261107_%E5%85%89%E8%8A%92%E5%9B%9B%E5%B0%84%E7%9A%84%E8%8A%82%E6%97%A5.jpg)<br>2026-11-07 | [![2026-11-06](thumbs/20261106_%E5%BD%92%E6%9D%A5%E7%9A%84%E8%8D%89%E5%8E%9F%E5%B7%A8%E5%85%BD.jpg)](pics/20261106_%E5%BD%92%E6%9D%A5%E7%9A%84%E8%8D%89%E5%8E%9F%E5%B7%A8%E5%85%BD.jpg)<br>2026-11-06 |
| [![2026-11-05](thumbs/20261105_%E7%A9%BF%E8%B6%8A%E6%AF%9B%E4%BC%8A%E5%B2%9B%E7%9A%84%E7%BB%BF%E8%89%B2%E9%9A%A7%E9%81%93.jpg)](pics/20261105_%E7%A9%BF%E8%B6%8A%E6%AF%9B%E4%BC%8A%E5%B2%9B%E7%9A%84%E7%BB%BF%E8%89%B2%E9%9A%A7%E9%81%93.jpg)<br>2026-11-05 |  |  |  |

<!-- GALLERY-END -->

## Manual actions

- Run it now: Actions tab → Bing Daily Wallpaper → Run workflow
- Run the script locally: `python3 bing_wallpaper.py 8 -o pics` (last 8 days; the number can be 1–8)

## Notes

- Schedule: Sundays 00:15 UTC. Each run fetches the last 8 days (the past week plus one spare day in case a run is missed; images already present are skipped). Scheduled runs may start some minutes late when GitHub is busy — that is normal.
- A UHD image is about 1–3 MB, so the repository grows by roughly 0.5–1 GB per year.
