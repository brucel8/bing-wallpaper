#!/usr/bin/env python3
"""Generate thumbnails and refresh the README gallery section.

Called by GitHub Actions after the wallpapers are downloaded; can also
be run manually:
    python3 make_gallery.py

- Thumbnails go to thumbs/ (400px wide); only images without one are
  processed
- The section of README.md between <!-- GALLERY-START --> and
  <!-- GALLERY-END --> is rewritten every run:
  * the latest month is shown expanded as a thumbnail grid
    (4 per row, click a thumbnail to open the full image)
  * earlier months are folded into <details> blocks, expanded only
    when the month title is clicked, so the README stays fast to
    open no matter how many images accumulate
"""
import calendar
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


def month_label(key: str) -> str:
    return f"{calendar.month_name[int(key[4:])]} {key[:4]}"


def table_for(files) -> str:
    cells = []
    for p in files:
        date = f"{p.name[:4]}-{p.name[4:6]}-{p.name[6:8]}"
        cells.append(
            f"[![{date}](thumbs/{quote(p.name)})](pics/{quote(p.name)})"
            f"<br>{date}")
    rows = []
    for i in range(0, len(cells), COLS):
        chunk = cells[i:i + COLS]
        chunk += [""] * (COLS - len(chunk))
        rows.append("| " + " | ".join(chunk) + " |")
    return "| | | | |\n|---|---|---|---|\n" + "\n".join(rows)


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

    months = {}
    for p in files:
        months.setdefault(p.name[:6], []).append(p)
    keys = sorted(months, reverse=True)

    if not keys:
        gallery = "_No images yet_"
    else:
        parts = []
        latest = keys[0]
        parts.append(
            f"### {month_label(latest)} (latest month)\n\n"
            + table_for(months[latest]))
        for k in keys[1:]:
            label = f"{month_label(k)} · {len(months[k])} images"
            parts.append(
                f"<details>\n<summary>{label} (click to expand)</summary>\n\n"
                + table_for(months[k]) + "\n\n</details>")
        gallery = "\n\n".join(parts)

    text = README.read_text(encoding="utf-8")
    pre, sep, rest = text.partition(START)
    if not sep:
        raise SystemExit("GALLERY markers not found in README.md")
    _, _, post = rest.partition(END)
    README.write_text(pre + START + "\n\n" + gallery + "\n\n" + END + post,
                      encoding="utf-8")
    print(f"gallery updated: {len(files)} images, {len(keys)} months")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
