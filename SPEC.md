# LW Lab 实验室网站 · 内容与设计规格（SPEC）

> 本文件是本网站唯一的**内容与设计依据**。建设者（人或 AI）必须严格遵守本文件。
> 本文件由实验室成员提供并维护，修改名单请直接编辑本文件。

---

## 1. 基本信息

| 项目 | 内容 |
|---|---|
| 实验室名称（主标识） | **LW Lab** |
| 中文名称 | **无限奇迹实验室** |
| 英文全称 | Limitless Wonder Laboratory |
| 建议副标题/Hero 文案 | Limitless Wonder · 无限奇迹实验室 |
| 语气基调 | 学术、克制、干净；不使用营销腔和夸张形容词 |

**注意：** L 与 W 的来源（两位导师姓名首字母）**不要**在网站任何位置展示或解释。

---

## 2. 设计风格（硬性要求）

- **背景**：纯白 `#FFFFFF`，大量留白。
- **整体**：极简学术风，参考国际高校课题组主页（如 Stanford / MIT CSAIL 实验室页）。
- **文字**：正文深灰近黑（`#1a1a1a` 或 `#222`）；辅助信息灰（`#666` / `#999`）。
- **强调色**：全场**至多一种**，建议学术深蓝 `#1a3a6b` 或深红 `#8b1e24`，仅用于链接、hover、细分隔线。
- **字体**：标题可用衬线（如 Noto Serif SC / 思源宋体），正文用无衬线；**必须使用系统字体栈回退**（如 `"Source Han Serif SC", "Noto Serif SC", "STZhongsong", serif`），**完全离线可打开，不依赖任何 CDN 或外链资源**。
- **布局**：单页 `index.html` + 顶部固定导航栏 + 锚点平滑滚动；内容区最大宽度 1080–1200px 居中；分区之间用细横线或留白分隔。
- **禁止**：大面积彩色色块、渐变背景、轮播图堆砌、弹窗、过重动画。
- **响应式**：手机（约 375px）/ 平板（约 768px）/ 桌面（≥1280px）三档不破版。
- 所有文件统一 **UTF-8** 编码。

---

## 3. 页面结构（单页 + 锚点导航）

| # | 导航项 | 内容 |
|---|---|---|
| 1 | 首页 Home | Hero 区：LW Lab / 无限奇迹实验室 / Limitless Wonder + 一句话学术简介 |
| 2 | 关于 About | 实验室简介 200–300 字，学术口吻；未知细节用`【待补充】`标记，不要编造具体事实（如成立年份、地址、经费） |
| 3 | 研究 Research | 3–4 个研究方向卡片；用通用学术化占位描述 + `【待补充】`标记 |
| 4 | 团队 People | 见 §4，导师在前、学生在后，共 22 人，**不得增删** |
| 5 | 新闻 News | 区块保留；可放 1–2 条占位示例并标注`【示例，待替换】`，或优雅空状态 |
| 6 | 加入我们 Join Us | 欢迎语 + 联系邮箱等联系方式用`【待补充】`占位 |
| 7 | Footer | `© 2026 LW Lab · 无限奇迹实验室`；不写备案号 |

---

## 4. 团队成员（共 22 人，顺序如下，后续可再调整）

### 4.1 导师 Faculty（2 人，置于团队区最前，卡片样式可稍大）

| 姓名 | 拼音（展示用） | 职称 | 照片文件名 |
|---|---|---|---|
| 刘立鸿 | Lihong Liu | 导师【职称待补充】 | `assets/photos/lihong-liu.jpg` |
| 王茜 | Qian Wang | 导师【职称待补充】 | `assets/photos/qian-wang.jpg` |

### 4.2 学生 Students（20 人）

| 姓名 | 拼音（展示用） | 照片文件名 |
|---|---|---|
| 张玙璠 | Yufan Zhang | `assets/photos/yufan-zhang.jpg` |
| 郑鑫浩 | Xinhao Zheng | `assets/photos/xinhao-zheng.jpg` |
| 刘纯海 | Chunhai Liu | `assets/photos/chunhai-liu.jpg` |
| 陈翀 | Chong Chen | `assets/photos/chong-chen.jpg` |
| 徐晨夏 | Chenxia Xu | `assets/photos/chenxia-xu.jpg` |
| 朱天昊 | Tianhao Zhu | `assets/photos/tianhao-zhu.jpg` |
| 李彤彤 | Tongtong Li | `assets/photos/tongtong-li.jpg` |
| 王创 | Chuang Wang | `assets/photos/chuang-wang.jpg` |
| 贾诗瑗 | Shiyuan Jia | `assets/photos/shiyuan-jia.jpg` |
| 石兰芳 | Lanfang Shi | `assets/photos/lanfang-shi.jpg` |
| 董豹 | Bao Dong | `assets/photos/bao-dong.jpg` |
| 韩娟 | Juan Han | `assets/photos/juan-han.jpg` |
| 罗红炜 | Hongwei Luo | `assets/photos/hongwei-luo.jpg` |
| 周世雄 | Shixiong Zhou | `assets/photos/shixiong-zhou.jpg` |
| 代欣 | Xin Dai | `assets/photos/xin-dai.jpg` |
| 李璟婕 | Jingjie Li | `assets/photos/jingjie-li.jpg` |
| 陈由洲 | Youzhou Chen | `assets/photos/youzhou-chen.jpg` |
| 张舒艳 | Shuyan Zhang | `assets/photos/shuyan-zhang.jpg` |
| 王梓焱 | Ziyan Wang | `assets/photos/ziyan-wang.jpg` |
| 王紫璇 | Zixuan Wang | `assets/photos/zixuan-wang.jpg` |

> 拼音按标准汉语拼音生成，个别生僻字读音（如 翀/瑗/璟/焱/玙璠）如与本人习惯不符，由成员后续在本文件中自行更正。

### 4.3 成员卡片要求（每人）

- 卡片结构：**上方照片预留位**（正方形或 3:4），下方居中**中文名** + 小号灰色**拼音**。
- 照片预留位：浅灰底（`#f0f0f0` 左右）、圆角、无照片时居中显示**姓氏首字**（如 `张`，浅灰衬线字）。
- 图片按 `<img src="assets/photos/{文件名}">` 结构输出，加载失败（onerror）时回退显示姓氏首字占位——这样以后把真实照片按 §4 的文件名放进 `assets/photos/` 即可自动显示，无需改代码。
- `assets/photos/` 目录已存在（内含 README），当前为空是正常的。

---

## 5. 技术要求（硬性）

- **纯静态站点**：`index.html` + `css/style.css` + `js/main.js`（JS 可选、尽量少）。
- **禁止**构建工具（webpack/vite 等）、前端框架（React/Vue 等）、外链 CDN。
- 不依赖网络即可完整浏览（双击 `index.html` 用 `file://` 也能打开）。
- 目录结构（本文件夹内）：

```
lab-website/
├── SPEC.md            # 本规格书（勿删）
├── PROGRESS.md        # 建设进度记录（断点续作用，由建设者维护）
├── REPORT.md          # 完工报告（完成后生成）
├── index.html
├── css/style.css
├── js/main.js
└── assets/photos/     # 成员照片，按 §4 文件名放置即可自动显示
```

---

## 6. 验收标准（全部满足才算完成）

1. 双击 `index.html` 或用任意静态服务器打开，整站完整可浏览。
2. 所有导航锚点跳转正确，无死链接、无 404 资源引用。
3. 浏览器控制台无 JS 报错。
4. 22 名成员全部渲染，顺序与 §4 一致，每人均有照片预留位。
5. 375 / 768 / 1440px 三种视口宽度下布局不破版。
6. 中文无乱码；风格符合 §2（白底、留白、学术感）。
