# Awesome CN MCP · 中文 MCP 服务桥接目录

> 把「中国服务 / 中国数据 / 中国语境」暴露给 AI 的 MCP 服务器精选目录。
> 每条目均经 GitHub API **实核验**，星数为 **2026-09-25 快照**，会随真实热度漂移。

---

## 为什么有这个目录（核心判断）

做需求信号扫描时，我们发现一个被低估的真实缺口：

- 英文 `punkpeye/awesome-mcp-servers` = **95,499★**；
- 中文 MCP 目录**并非不存在，但是极小且基本未策展**——最佳 `zackchewa/awesome-china-mcp` 仅 **13★**，另有 2 个 0★ 仓库；
- 更锋利的发现：**真正「中国服务 → AI 桥接」的 MCP 实体只有约 15 个**，且几乎全是 ≤400★ 的业余级项目，微信 / 抖音 / 小红书等核心 C 端服务桥接无官方维护。

结论：中文 MCP 生态的瓶颈不在「有没有目录」，而在**中国本土服务 / 数据的桥接供给本身稀疏且业余**。本目录不做大而全的链接堆，只做**可核验、带质量判读**的精选。

---

## 数据快照与诚实边界

- 星数快照日：**2026-09-25**，来源 GitHub Search / REST API。
- `repo 数 ≠ 可用供给`：列名存在 ≠ 能跑通 ≠ 维护中。每条目标注凭据要求与 `last_push`（见 `scripts/verify.py`）。
- 缺口真实 ≠ 需求大：我们曾验证「支付宝支付 MCP」看似真空，实则**支付宝官方已发布** `alipay/global-alipayplus-mcp`（8★）——数量少可能是「已被官方解决」，动手造前必验。

---

## 目录

### 一、中国互联网服务桥接

**即时通讯 / IM**

| 服务 | 仓库 | ★(快照) | 凭据 | 备注 |
|---|---|---:|---|---|
| 微信 WeChat | `1052666/WeChat-MCP-Server` | 35 | 登录 | NT 架构提醒助手 |
| 微信 | `LinnnnYue/weixin-mcp-server` | 1 | 登录 | 基于 pyweixin |
| 企业微信 WeCom | `emilywudreamer/wecom-mcp-server` | 0 | Token | 通讯录/消息/文档/日程 |

**内容 / 社交**

| 服务 | 仓库 | ★(快照) | 凭据 | 备注 |
|---|---|---:|---|---|
| 飞书 Feishu/Lark | `cso1z/Feishu-MCP` | 740 | Token | 文档与任务，CLI+Skill |
| 抖音 Douyin | `lancelin111/douyin-mcp-server` | 35 | — | 视频上传 |
| 抖音/TikTok | `Evil0ctal/Douyin_TikTok_Download_API` | 20321 | 自托管 | 无水印下载，MCP-capable |
| 小红书 Xiaohongshu | `aicu-icu/xhs-mcp-server` | 182 | — | 笔记搜索/通知 |
| 大众点评 Dianping | `shawnq-msft/mcp-dianping` | 2 | — | MS 示例，本地搜索 |

**地图 / LBS**

| 服务 | 仓库 | ★(快照) | 凭据 | 备注 |
|---|---|---:|---|---|
| 高德 Amap | `blacsheep/LLM-Amap-mcp` | 6 | Key | 地址服务 ⚠️弃更(>12月) |
| 高德 Amap（应用） | `bamboo-moon/zhisaotong-Agent` | 141 | Key | 旅游助手 |

**生活服务**

| 服务 | 仓库 | ★(快照) | 凭据 | 备注 |
|---|---|---:|---|---|
| 印象笔记中国 Yinxiang | `ArchChuan/yinxiang-mcp` | 2 | 登录 | 非官方 |
| 佳明中国 Garmin CN | `xinyuxinyuxintaihaohao/garmin-cn-mcp` | 4 | 登录 | 数据读取 |
| 麦当劳中国 McDonald's CN | `M-China/mcd-mcp-server` | 139 | — | 集成指南 |
| 支付宝 Alipay（官方） | `alipay/global-alipayplus-mcp` | 8 | — | 官方，global/alipayplus ⚠️弃更(>12月) |

### 二、中国数据 / 金融

| 主题 | 仓库 | ★(快照) | 凭据 | 备注 |
|---|---|---:|---|---|
| 股票/加密货币 | `aahl/mcp-aktools` | 391 | — | 数据查询分析 |
| A股/美股/加密货币 | `huweihua123/stock-mcp` | 177 | — | 金融市场数据 |

### 三、中国开发者工具

| 主题 | 仓库 | ★(快照) | 凭据 | 备注 |
|---|---|---:|---|---|
| 蓝湖需求分析 | `dsphper/lanhu-mcp` | 2421 | Token | 团队协作 AI 编程 |
| 中文开发套件 | `cfrs2005/claude-init` | 1362 | — | Claude Code 中文化 |
| Android/Win 自动化 | `MAA-AI/MaaMCP` | 385 | — | 基于 MaaFramework |
| MCP 管理桌面端 | `skrstop/MCPHub-Desktop` | 438 | — | 本地统一管理 |

### 四、中国语境 / 文化数据源（本目录重点缺口层）

| 主题 | 仓库 | ★(快照) | 凭据 | 备注 |
|---|---|---:|---|---|
| 古诗文/节假日/历史上的今天 | `mouseart2025/china-context-mcp` | 0 | 零凭据 | 沙箱可跑通，本目录维护方出品 |

### 五、基础框架 / 工具（全球，必装）

| 主题 | 仓库 | ★(快照) | 备注 |
|---|---|---:|---|
| Python MCP 框架 | `PrefectHQ/fastmcp` | 27894 | 本目录所有 Python 服务端基线 |
| MCP 可视化调试 | `modelcontextprotocol/inspector` | 10950 | 联调必备 |

---

## 覆盖度判读（诚实）

- **真正「中国服务 → AI 桥接」实体 ≈ 15 个**；≥1000★ 仅 3 个（`lanhu` 2421、`claude-init` 1362、`Douyin_TikTok_Download_API` 20321——但后者是下载器而非纯桥接）。
- 微信 / 抖音 / 小红书等**核心 C 端服务桥接多为 ≤35★ 业余项目，无官方维护**，稳定性与合规风险自担。
- **官方桥接仅支付宝一例**（8★，且是 global/alipayplus，非国内收单全量）；更刺眼的是**该官方仓 `last_push` 已 >12 个月未更新**——连官方都未持续维护。
- **弃更普遍**：收录项中 `blacsheep/LLM-Amap-mcp`（高德）、`alipay/global-alipayplus-mcp`（支付宝）均已 >12 月未推；多数 C 端桥接为个人业余维护，停产风险高。
- **政务 / 公共数据桥接极度稀缺**：天气、空气质量、节假日、教科书、法规等几乎无人维护；`china-context-mcp` 是此层少有的零凭据可跑通样本。

---

## 策展标准

1. **真实可核验**：每条目经 GitHub API 核验存在 + 抓取星数快照（见 `scripts/verify.py`）。
2. **零凭据优先**：标注是否需要 API key / 登录；零凭据项优先置顶。
3. **中国相关性**：服务源或主要用户群在中国。
4. **非官方垄断校验**：收录前先确认缺口真实，避免与官方实现撞车（如支付宝）。
5. **运维信号**：标注 `last_push`；弃更（>12 月未推）项目打 ⚠️。

---

## 如何验证本目录

```bash
python scripts/verify.py        # 逐条复核验名 + 星数漂移 + 失效链接
```

`verify.py` 读取 `data/registry.json`，对每条目调用 `gh api` 复核存在性与当前星数；任一链接失效即以非零码退出。

---

## 相关项目

- `zackchewa/awesome-china-mcp`（13★）— 早期中文 MCP 列表，可作补充参阅。
- `punkpeye/awesome-mcp-servers`（95,499★）— 英文总目录，本目录不重复其通用条目。

---

## 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。新条目须附带可核验仓库地址，并同步更新 `data/registry.json`。

## License

[MIT](LICENSE)
