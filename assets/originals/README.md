# assets/originals/ — 原始大图归档

本文件夹存放**未经压缩的原始大图**（相机直出 / 原始设计稿）。网站**不直接引用**这里的文件。

## 当前文件

归档的原始图（网页压缩版见 `../photos/`）：`合照.jpg`、`合照2.jpg`、`ziyan-wang.png`、
`xuchen-xia.jpg`、`chong-chen.jpg`、`bao-dong.png` 及少量压缩过程中的中间版本（`*_1.jpg`）。

## 自动处理

直接把新图丢进 `assets/photos/`（文件名按 SPEC §4.2），然后运行：

    python tools/check_images.py        # 加 --dry-run 只预览

脚本会自动：尺寸超标（横图>1920px / 竖图>1200px）或 PNG 的 → 压缩回 `photos/`（质量 85，
PNG 平铺白底转 JPG），原图移入本文件夹；文件名含 "logo" 的跳过；可重复运行。

原始文件请保留：它是未来重新压缩、印刷或出具高清版的源头。
