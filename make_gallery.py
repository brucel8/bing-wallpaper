#!/usr/bin/env python3
"""生成缩略图并刷新 README 图库区。

由 GitHub Actions 在下载壁纸后调用，也可本地手动运行：
    python3 make_gallery.py

- 缩略图放 thumbs/（宽 400px），只给还没有缩略图的图片生成
- README.md 中 <!-- GALLERY-START --> 与 <!-- GALLERY-END --> 之间的
  表格会被整段重写：每行 4 张，点缩略图打开原图
"""
from pathlib import Path
from urllib.parse import quote

from PIL import Image

ROOT = Path(__file__).resolve().parent
PICS = ROOT / "pics"
THUMBS = ROOT / "thumbs"
README = ROOT / "README.md"
START, END = "<!-- GALLERY-START -->", "<!-- GALLERY-END -->"
THUMB_W = 400
COLS = 4


def main() -> int:
    THUMBS.mkdir(exist_ok=True)
    files = sorted(PICS.glob("*.jpg"), reverse=True)
    for p in files:
        t = THUMBS / p.name
        if t.exists() and t.stat().st_size > 5_000:
            continue
        with Image.open(p) as im:
            im = im.convert("RGB")
            w, h = im.size
            im.resize((THUMB_W, max(1, int(h * THUMB_W / w)))).save(
                t, quality=82)
    cells = []
    for p in files:
        date = f"{p.name[:4]}-{p.name[4:6]}-{p.name[6:8]}"
        cells.append(
            f"[![{date}](thumbs/{quote(p.name)})](pics/{quote(p.name)})"
            f"<br>{date}")
    if cells:
        rows = []
        for i in range(0, len(cells), COLS):
            chunk = cells[i:i + COLS]
            chunk += [""] * (COLS - len(chunk))
            rows.append("| " + " | ".join(chunk) + " |")
        table = "| | | | |\n|---|---|---|---|\n" + "\n".join(rows)
    else:
        table = "_暂无图片_"
    text = README.read_text(encoding="utf-8")
    pre, sep, rest = text.partition(START)
    if not sep:
        raise SystemExit("README.md 里找不到 GALLERY 标记")
    _, _, post = rest.partition(END)
    README.write_text(pre + START + "\n\n" + table + "\n\n" + END + post,
                      encoding="utf-8")
    print(f"gallery updated: {len(files)} images")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
