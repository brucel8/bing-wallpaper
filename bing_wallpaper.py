#!/usr/bin/env python3
"""下载必应每日壁纸（超清 4K，失败回退 1080p）。

用法:
    python bing_wallpaper.py            # 今天 1 张
    python bing_wallpaper.py 8          # 最近 8 天
    python bing_wallpaper.py 8 -o D:/Pictures/Bing
"""
import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

API = "https://www.bing.com/HPImageArchive.aspx?format=js&idx={idx}&n={n}&mkt=zh-CN"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def safe(name: str) -> str:
    return re.sub(r'[\\/:*?"<>|]', "_", name).strip()[:60]


def download(url: str, dest: Path) -> bool:
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
        if len(data) < 50_000:
            return False
        dest.write_bytes(data)
        return True
    except Exception:
        return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("count", nargs="?", type=int, default=1, help="下载最近几天的壁纸 (1-8)")
    ap.add_argument("-o", "--out", default="BingWallpapers", help="保存目录")
    args = ap.parse_args()

    count = max(1, min(args.count, 8))
    out_dir = Path(args.out).expanduser()
    out_dir.mkdir(parents=True, exist_ok=True)

    images = fetch_json(API.format(idx=0, n=8))["images"][:count]
    ok = 0
    for img in images:
        stem = safe(f"{img['startdate']}_{img.get('title', 'bing')}")
        dest = out_dir / f"{stem}.jpg"
        if dest.exists() and dest.stat().st_size > 50_000:
            print(f"跳过（已存在）: {dest.name}")
            ok += 1
            continue
        for suffix in ("_UHD.jpg", "_1920x1080.jpg"):
            if download("https://www.bing.com" + img["urlbase"] + suffix, dest):
                size = dest.stat().st_size
                print(f"已保存: {dest.name}  ({size / 1024 / 1024:.1f} MB)  {img.get('copyright', '')}")
                ok += 1
                break
        else:
            print(f"失败: {img['startdate']}", file=sys.stderr)

    print(f"\n完成 {ok}/{len(images)}，目录: {out_dir.resolve()}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
