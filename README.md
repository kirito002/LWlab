# LW Lab · 无限奇迹实验室

在线网站：https://kirito002.github.io/LWlab/

## 平时只维护一个内容文件

**website-content.json 是网站内容源文件**，用记事本或代码编辑器打开即可。包含首页文字、最新论文卡片、实验室介绍、合影、研究方向、两位导师简介、成员、新闻、招募联系方式以及论文列表。

修改引号里的文字，保留双引号、逗号和括号。换行用 `\n`，文中的双引号用 `\"`；正文需要加粗时用 `**文字**`。数组中的项目按显示顺序排列，新闻和论文年份自动倒序。

| 修改内容 | 搜索字段 |
|---|---|
| 新闻 | `news`；复制一条，填写 `date`（YYYY-MM）、`title`、`detail` |
| 两位导师简介 | `faculty`；第一位在左，第二位在右 |
| 成员、照片文件名 | `people` |
| 首页最新论文展示 | `latest_publications` |
| 全部论文 | `publications`；按年份添加 `entries`，共同署名论文只收录一次 |
| 关于、研究、联系方式 | `about`、`research`、`join` |

修改后可以让 Codex“同步内容文件到网页”，或者在本目录运行：

```powershell
python tools/sync_content.py
```

同步脚本仅使用 Python 标准库，把内容写回 index.html 和 publication.html，并自动更新图片、CSS、JS 的缓存版本。`python tools/sync_content.py --check` 可检查是否已同步。请勿直接修改生成区域内的 HTML 文案，下次同步会覆盖。

## 更新照片

按内容文件中的路径放到 assets/photos/。运行 `python tools/check_images.py`（需要 Pillow）：超尺寸图片压缩后放回，原图自动归档到 assets/originals/，小图不变。再运行内容同步脚本以刷新缓存版本。

## 预览与上线

直接双击 index.html，或运行 `python -m http.server 8765` 后访问 http://localhost:8765 。网站仍是纯 HTML/CSS/JS，无前端框架、构建工具或 CDN；Python 只用于维护，访客和 GitHub Pages 不需要 Python。

确认页面后提交并推送到 GitHub，由现有 GitHub Pages 配置发布。原始导师简历保留在网站目录之外，不纳入 Git。

设计规则见 SPEC.md，修改记录见 PROGRESS.md。旧的 assets/publication-old.txt 和 assets/photos/publication/paper-info.txt 仅作历史参考，当前内容以 website-content.json 为准。
