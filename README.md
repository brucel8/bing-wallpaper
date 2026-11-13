# Bing Daily Wallpaper

每周日自动把过去一周的 Bing 每日壁纸（4K UHD，失败回退 1080p）下载存进本仓库，由 GitHub Actions 定时执行，本地电脑不用开机。

- 全部图片在 `pics/` 目录，按 `日期_标题.jpg` 命名
- `latest.jpg` 永远指向最新一张，也就是下面这张

![今日壁纸](latest.jpg)

## 图库（点缩略图看原图）

<!-- GALLERY-START -->

_暂无图片_

<!-- GALLERY-END -->

## 手动操作

- 补跑一次：仓库 Actions 页 → Bing Daily Wallpaper → Run workflow
- 本地运行脚本：`python3 bing_wallpaper.py 8 -o pics`（拉最近 8 天；数字可改 1–8）

## 说明

- 定时任务时间：每周日 UTC 00:15（北京时间周日 08:15），一次拉最近 8 天（覆盖上周 7 天，另 1 天冗余防漏；已下载的自动跳过）。GitHub 排队繁忙时可能延迟几十分钟，属正常
- UHD 图片约 1–3 MB/张，仓库体积每年约增长 0.5–1 GB
