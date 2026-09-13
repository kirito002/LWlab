# assets/icons/ — 研究方向图标

来源：[Tabler Icons](https://github.com/tabler/tabler-icons)（MIT 许可证，可自由使用），
已将描边色改为实验室强调色 `#1a3a6b`，本地存放、无外链，离线可用。

| 文件 | 用于 | Tabler 名称 |
|---|---|---|
| `virus.svg` | 病毒进化与免疫应答 | `virus` |
| `arrows-exchange.svg` | 病毒与宿主相互作用 | `arrows-exchange` |
| `microscope.svg` | 病原诊断与抗体药物 | `microscope` |
| `vaccine.svg` | 疫苗设计与基因治疗 | `vaccine` |

换图标：从 Tabler Icons 官网挑选同名 SVG 下载覆盖，再执行
`sed -i 's/stroke="currentColor"/stroke="#1a3a6b"/g' assets/icons/*.svg` 统一着色，
并把 index.html 里 css 的 `?v=` 版本号加一。
