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
  > **2026-09-11 修订**：经实验室确认，新增两处例外——① Hero 区 LW 徽标**粒子交互动画**（鼠标靠近散开、移开复原，参考 deepseek.com/harness 鲸鱼效果；白底、取徽标原色，不算"过重动画"）；② "关于"区**合影轮播**（2 张，自动 + 手动滚动）。除此之外设计约束不变。
- **响应式**：手机（约 375px）/ 平板（约 768px）/ 桌面（≥1280px）三档不破版。
- 所有文件统一 **UTF-8** 编码。

---

## 3. 页面结构（单页 + 锚点导航）

| # | 导航项 | 内容 |
|---|---|---|
| 1 | 首页 Home | Hero 区**左右分栏**：左侧 = LW 徽标粒子动画 + 标题/简介；右侧 = "最新发表"论文展示卡（图 + 题目 + 作者/期刊，来自 `assets/photos/publication/paper-info.txt`；多篇时自动轮播，卡下注明添加方法） |
| 2 | 关于 About | 实验室简介 200–300 字，学术口吻；末尾附**合影轮播**（§4.0）；未知细节用`【待补充】`标记，不要编造具体事实（如成立年份、经费） |
| 3 | 研究 Research | 3–4 个研究方向卡片；**2026-09-11 已替换为真实方向**（病毒进化与免疫应答 / 病毒与宿主相互作用 / 病原诊断与抗体药物 / 疫苗设计与基因治疗），依据两位导师的研究领域综述；卡片标题配 Tabler 线性图标（`assets/icons/`，MIT，已本地化改色，见该目录 README） |
| 4 | 团队 People | 见 §4：导师在前，学生按 **博士 → 博士后 → 硕士** 分组（每组标身份不标年级），共 21 人，**不得自行增删** |
| 5 | 新闻 News | 区块保留；**2026-09-11 已录入**：网站上线（2026-09）、Journal of Infection 论文（2026-08，doi:10.1016/j.jinf.2026.106827）；后续新闻按此格式追加 |
| 6 | 论文 Publication | **独立整页 `publication.html`**（2026-09-12 新增）：导师既往发表论文（源自 `assets/publication-old.txt`），按年份倒序，**去重合并**（共同署名论文只列一次，共 43 篇，含 2026 最新发表）；**实验室成员姓名（Wang Q / Liu L）与期刊名加粗**；* 通讯作者、# 共同第一作者 |
| 7 | 加入我们 Join Us | 欢迎语 + 联系方式；**已填**：邮箱 llh3411@whu.edu.cn，**实验室位置：武汉大学生命科学学院 4013、4017 实验室** |
| 8 | Footer | `© 2026 LW Lab · 无限奇迹实验室 · 武汉大学 & 泰康生命医学中心`；不写备案号 |
| 7 | Footer | `© 2026 LW Lab · 无限奇迹实验室`；不写备案号 |

---

## 4. 团队成员（共 21 人，顺序如下，后续可再调整）

### 4.1 导师 Faculty（2 人，置于团队区最前，卡片样式可稍大）

| 姓名 | 拼音（展示用） | 职称 | 照片文件名 |
|---|---|---|---|
| 刘立鸿 | Lihong Liu | 教授（生科院与泰康生命医学中心双聘） | `assets/photos/lihong-liu.jpg` |
| 王茜 | Qian Wang | 教授 | `assets/photos/qianwang.jpg` |

> **2026-09-11 新增**：导师卡片下方各有一张**完整简介卡**（学科专业 / 研究方向 / 实验室位置 / Email +
> 学习经历 / 工作经历 / 奖励荣誉 / 研究领域兴趣；王茜另含主持课题与研究生信息），内容由实验室提供，
> 展示文案以简介卡为准；点击导师卡片可锚点跳转到对应简介卡。

### 4.0 徽标与合影（2026-09-11 新增）

| 文件 | 用途 |
|---|---|
| `assets/photos/LWlab.jpg` | 实验室徽标：顶栏 logo、favicon、Hero 粒子动画源图（粒子代码内嵌其 base64，修改徽标后需同步 `js/main.js` 中的 data URI） |
| `assets/photos/group-1.jpg?v=N` | 合影轮播图 1（由 `合照.jpg` 压缩，1920px/85%） |
| `assets/photos/group-2.jpg?v=N` | 合影轮播图 2（由 `合照2.jpg` 压缩，1920px/85%） |

- 轮播行为：每 4.5 秒自动滚动到下一张；悬停暂停；手动操作（按钮 / 圆点 / 触摸滑动）后暂停 8 秒再恢复自动。
- **替换照片时**：把原始大图放入 `assets/originals/`，压缩后覆盖 `photos/` 对应文件，并把 HTML 里 `?v=N` 版本号加一。
- 原始大图自 2026-09-12 起统一放 `assets/originals/`（详见其 README）；网页只引用 `photos/` 内压缩版。

### 4.2 学生 Students（19 人，按 博士 → 博士后 → 硕士 分组展示）

> **排序与标签（2026-09-12 实验室名单确认）**：按 **博士研究生(PhD) → 博士后(Postdoc) → 硕士研究生(Master)**
> 分组；只标身份不标年级（研一/研二/研三→Master，博一/博二/博三→PhD），卡片副标题为 `拼音 · PhD/Postdoc/Master`。
> 无实习生。罗红炜不在实验室提供的名单中，2026-09-13 按实验室要求从团队中移除。

| 姓名 | 拼音（展示用） | 角色 | 照片文件名 |
|---|---|---|---|
| 陈翀 | Chong Chen | 博士 PhD | `assets/photos/chong-chen.jpg` |
| 朱天昊 | Tianhao Zhu | 博士 PhD | `assets/photos/tianhao-zhu.jpg` |
| 王创 | Chuang Wang | 博士 PhD | `assets/photos/chuang-wang.jpg` |
| 董豹 | Bao Dong | 博士 PhD | `assets/photos/bao-dong.jpg` |
| 代欣 | Xin Dai | 博士 PhD | `assets/photos/xin-dai.jpg` |
| 张舒艳 | Shuyan Zhang | 博士 PhD | `assets/photos/shuyan-zhang.jpg` |
| 刘纯海 | Chunhai Liu | 博士 PhD | `assets/photos/chunhai-liu.jpg` |
| 徐晨夏 | Chenxia Xu | 博士 PhD | `assets/photos/xuchen-xia.jpg` |
| 石兰芳 | Lanfang Shi | 博士 PhD | `assets/photos/shilan-fang.jpg`（750×750 方图，3:4 容器会左右裁切） |
| 韩娟 | Juan Han | 博士 PhD | `assets/photos/juan-han.jpg` |
| 周世雄 | Shixiong Zhou | 博士后 Postdoc | `assets/photos/shixiong-zhou.jpg` |
| 张玙璠 | Yufan Zhang | 硕士 Master | `assets/photos/yufan-zhang.jpg` |
| 贾诗瑗 | Shiyuan Jia | 硕士 Master | `assets/photos/shiyuan-jia.jpg` |
| 王梓焱 | Ziyan Wang | 硕士 Master | `assets/photos/ziyan-wang.jpg`（由用户提供的 `ziyan-wang.png` 压缩转制，1200px/88%） |
| 王紫璇 | Zixuan Wang | 硕士 Master | `assets/photos/zixuan-wang.jpg` |
| 李彤彤 | Tongtong Li | 硕士 Master | `assets/photos/tongtong-li.jpg` |
| 李璟婕 | Jingjie Li | 硕士 Master | `assets/photos/jingjie-li.jpg` |
| 陈由洲 | Youzhou Chen | 硕士 Master | `assets/photos/youzhou-chen.jpg` |
| 郑鑫浩 | Xinhao Zheng | 硕士 Master | `assets/photos/xinhao-zheng.jpg` |

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

---

## 7. 更新记录

- **2026-09-12**（六项修改）：
  - **粒子散开范围缩小**：鼠标斥力半径 100px → 46px（约鼠标处一个小圆圈），推力同步减弱。
  - **新增 `assets/originals/`**：原始大图统一归档（合照、合照2、ziyan-wang.png、xuchen-xia 原图、chong-chen 原图），
    网站只引用 `photos/` 内压缩版；流程见该文件夹 README。今后大图先进 originals，压缩后放回 photos。
  - **顶栏改版**：导航文字左移至 LW Lab 右侧；右上角放**武汉大学 + 泰康生命医学中心**两个单位徽标。
  - **Hero 左右分栏**：左侧粒子动画 + 标题简介；右侧"Latest Publication · 最新发表"展示卡（当前为
    JOI 2026 图摘要，信息按 `assets/photos/publication/paper-info.txt`；**新文章 = 复制一个
    `<article class="paper-slide">`，多于一张自动 7 秒轮播**）。
  - **新增 `publication.html`**：导师既往论文 42 篇（由 `assets/publication-old.txt` 去重合并——两位导师
    共同署名的 15 篇只列一次），按年份倒序，成员姓名与期刊名加粗；导航"论文"指向该页。
  - **加入我们**：实验室位置更新为**生科院 4013、4017 实验室**。
  - **2026-09-13 修订**：两位导师"实验室位置"统一为**生命科学学院 4017**（不再写泰康）；研究卡片新增 4 枚 Tabler 图标（本地 SVG，MIT）。
  - 学生照片补齐：陈翀（chong-chen.jpg）、石兰芳（shilan-fang.jpg，注意文件名是 shilan-fang 不是 lanfang-shi）。
  - 全站引用版本号递增为 `?v=20260912`。

- **2026-09-11**（内容与交互大版本）：
  - 新增 Hero 徽标粒子动画（`js/main.js`，纯手写 Canvas 物理，无依赖；徽标 data URI 内联以兼容 `file://`）。
  - 新增"关于"区合影轮播（CSS scroll-snap + 原生 JS，自动/手动滚动、圆点指示）。
  - 顶栏与 favicon 换用实验室徽标 `LWlab.jpg`。
  - 填入导师双简介卡、研究方向卡片、新闻（J Infect 论文）、加入我们联系方式。
  - 修正学生照片文件名与实际文件一致（`qianwang.jpg` / `xuchen-xia.jpg` / `ziyan-wang.jpg`）。
  - 新增压缩版网络图片（`group-1/2.jpg`、`ziyan-wang.jpg`），原始大图保留。
  - HTML 中 css/js/合影图引用带 `?v=20260911` 版本号：**更新任何被引用文件后请递增版本号**。
  - 验收记录：1440/768/375 视口无破版无横向溢出；`file://` 双击打开正常（Edge 实测）；控制台无 JS 报错；22 名成员完整渲染。
