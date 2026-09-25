# 贡献指南

本目录的核心承诺是**可核验**，不是链接数量。提交新条目请遵循以下流程。

## 条目资格

1. **中国相关性**：服务源或主要用户群在中国。
2. **真实可核验**：仓库必须存在且公开（`gh api repos/<owner>/<name>` 可返回）。
3. **非官方垄断校验**：动手造 / 收录前，先确认该服务没有被官方实现覆盖（参考支付宝案例）。
4. **凭据透明**：必须标注是否需要 API key / 登录 / 自托管。

## 提交流程

1. Fork 并克隆本仓库。
2. 编辑 `data/registry.json`，在对应 `category` 下新增条目：

   ```json
   {"repo": "owner/name", "service": "服务中文名", "category": "im|social|lbs|life|pay|finance|devtool|context|framework", "credential": "none|key|login|token|selfhost", "snapshot_stars": 0}
   ```

3. 运行核验脚本，确认无失效链接、星数已刷新：

   ```bash
   python scripts/verify.py
   ```

4. 在 `README.md` 对应分类表格中补充一行（★ 填 `verify.py` 输出的当前值）。
5. 提交 PR，标题格式：`add: owner/name — 服务名`。

## 弃更打标

若某条目 `last_push` 距快照日 > 12 个月，在 README 备注列加 ⚠️，不移除（保留历史信号）。

## 质量标准

- 不收录无法核验的博客 / 私链。
- 不重复 `punkpeye/awesome-mcp-servers` 的通用条目；本目录只收「中国相关」。
- 零凭据项优先置顶。
