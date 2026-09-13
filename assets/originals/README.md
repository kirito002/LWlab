# assets/originals/ — 原始大图归档

本文件夹存放**未经压缩的原始大图**（相机直出 / 原始设计稿）。网站**不直接引用**这里的文件。

## 当前文件

| 原始文件 | 大小 | 网页使用的压缩版 |
|---|---|---|
| `合照.jpg` | 6.7 MB（5328×4000） | `photos/group-1.jpg`（1920px / 85%） |
| `合照2.jpg` | 15.9 MB（6000×4000） | `photos/group-2.jpg`（1920px / 85%） |
| `ziyan-wang.png` | 23 MB PNG（3579×4130） | `photos/ziyan-wang.jpg`（1200px / 88%） |
| `xuchen-xia.jpg` | 3.0 MB（3072×4096） | `photos/xuchen-xia.jpg`（1200px / 85%） |
| `chong-chen.jpg` | 0.6 MB（1279×1617） | `photos/chong-chen.jpg`（1200px / 85%） |

## 使用流程

1. 新的大图放进本文件夹；
2. 用 PIL/ImageMagick 压缩到长边 ≤1920px（合影）/1200px（人像）、质量 85%，输出到 `assets/photos/`；
3. 如替换了网站已有图片，记得把 `index.html` 里对应的 `?v=N` 版本号加一。

原始文件请保留：它是未来重新压缩、印刷或出具高清版的源头。
