# LW Lab · 无限奇迹实验室

Limitless Wonder Laboratory 官方网站 · 依托武汉大学生命科学学院与泰康生命医学中心。

**在线访问**：<https://kirito002.github.io/LWlab/>

## 技术形态

纯静态站点（`index.html` + `publication.html` + `css/` + `js/`），零构建、零外部依赖，
系统字体栈 + 本地资源，`file://` 双击打开同样完整可用。改动后 `git push` 即自动重新部署（GitHub Pages）。

## 目录速览

| 路径 | 说明 |
|---|---|
| `index.html` | 主页（Hero 粒子动画 / 关于+合影轮播 / 研究 / 团队 / 新闻 / 加入我们） |
| `publication.html` | 论文列表页（全部发表，按年份倒序，去重收录） |
| `assets/photos/` | 网站引用的图片（压缩版，按 SPEC §4 文件名放置即自动显示） |
| `assets/icons/` | 研究方向图标（Tabler Icons，MIT） |
| `assets/originals/` | 原始大图归档（网页不直接引用） |
| `SPEC.md` | 内容与设计唯一规格书（改内容前先看它） |
| `PROGRESS.md` | 建设进度日志 |

## 更新内容

1. 直接编辑对应文件（成员照片放进 `assets/photos/` 即自动显示）；
2. 替换已有图片/样式时，记得把 HTML 引用里的 `?v=` 版本号加一；
3. `git add -A && git commit -m "..." && git push` —— 一分钟后线上生效。

内容规则（成员名单、分组、写作口径等）以 `SPEC.md` 为准。
