#!/usr/bin/env python3
"""LW Lab · assets/photos 图片体检脚本

扫描 assets/photos/ 下的图片，超标的自动压缩：
  - 处理条件：长边超过上限（横图 1920px / 竖图与方图 1200px），或是 PNG（体积常异常大，
    含透明通道则平铺白底转 JPG）
  - 原始文件移入 assets/originals/ 留档，压缩版（质量 85）写回 assets/photos/
  - 文件名含 "logo" 的跳过（logo 需保留原格式）
  - 脚本可重复运行：已达标的不做任何改动，不会反复重编码

用法：
    python tools/check_images.py            # 处理 assets/photos/
    python tools/check_images.py --dry-run  # 只预览将要做什么，不改动文件

依赖：Pillow（pip install pillow）
"""

import io
import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
PHOTOS = ROOT / "assets" / "photos"
ORIGINALS = ROOT / "assets" / "originals"
QUALITY = 85
LOGO_PATTERN = "logo"  # 文件名含 logo 的不处理


def limits_for(img):
    """横图（如合影）上限 1920px，竖图/方图（人像）上限 1200px。"""
    return 1920 if img.width > img.height else 1200


def unique_dest(directory: Path, name: str) -> Path:
    dst = directory / name
    i = 1
    while dst.exists():
        dst = directory / f"{Path(name).stem}_{i}{Path(name).suffix}"
        i += 1
    return dst


def process(path: Path, dry_run: bool):
    if LOGO_PATTERN in path.name.lower():
        return None

    im = Image.open(path)
    im = ImageOps.exif_transpose(im)
    limit = limits_for(im)
    oversized = im.width > limit or im.height > limit

    if not (oversized or path.suffix.lower() == ".png"):
        return None  # 达标，跳过

    if oversized:
        ratio = limit / max(im.width, im.height)
        im = im.resize((round(im.width * ratio), round(im.height * ratio)), Image.LANCZOS)

    if im.mode in ("RGBA", "P", "LA"):  # 透明通道平铺白底
        bg = Image.new("RGB", im.size, (255, 255, 255))
        rgba = im.convert("RGBA")
        bg.paste(rgba, mask=rgba.split()[-1])
        im = bg
    elif im.mode != "RGB":
        im = im.convert("RGB")

    out_name = path.stem + ".jpg"  # PNG 一律转 JPG
    old_kb = path.stat().st_size // 1024

    if dry_run:
        return f"[dry] {path.name} -> photos/{out_name} ({im.width}x{im.height})，原图移入 originals/"

    # 先在内存里完成压缩，再移走原图、写回压缩版——任何一步都不会误删照片
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=QUALITY, optimize=True, progressive=True)

    dst = unique_dest(ORIGINALS, path.name)
    path.replace(dst)                      # 原图 -> originals/
    out_path = path.with_name(out_name)
    out_path.write_bytes(buf.getvalue())   # 压缩版 -> photos/

    return (f"[ok ] {path.name} ({old_kb}KB) -> photos/{out_name} "
            f"({len(buf.getvalue()) // 1024}KB, {im.width}x{im.height})；原图 -> originals/{dst.name}")


def main():
    dry = "--dry-run" in sys.argv
    ORIGINALS.mkdir(exist_ok=True)

    files = sorted(p for p in PHOTOS.iterdir()
                   if p.is_file() and p.suffix.lower() in (".jpg", ".jpeg", ".png"))
    print(f"扫描 {len(files)} 张图片（{PHOTOS}）\n")
    changed = 0
    for p in files:
        result = process(p, dry)
        if result:
            print(result)
            changed += 1
    print(f"\n完成：{changed} 张需要处理，其余已达标。")


if __name__ == "__main__":
    main()
