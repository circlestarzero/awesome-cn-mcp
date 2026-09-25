#!/usr/bin/env python3
"""逐条复核 awesome-cn-mcp 收录的仓库：存在性 + 当前星数 + last_push。

读取 data/registry.json，对每条目调用 `gh api repos/<repo>` 复核。
任一链接失效即以非零码退出（可用于 CI 卡口）。
"""
import json
import subprocess
import sys

REG = "data/registry.json"


def gh(repo: str):
    """返回 {'stars':int,'pushed':str} 或 None（失效/私有/404）。"""
    r = subprocess.run(
        ["gh", "api", f"repos/{repo}", "--jq",
         "{stars:.stargazers_count,pushed:.pushed_at}"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except Exception:
        return None


def main() -> int:
    data = json.load(open(REG, encoding="utf-8"))
    snap = data.get("snapshot_date", "未知")
    print(f"awesome-cn-mcp 核验 @ 快照 {snap}\n")
    bad = 0
    for e in data["entries"]:
        repo = e["repo"]
        cur = gh(repo)
        if cur is None:
            print(f"  [404] {repo}  <- 链接失效 / 私有 / 拼写错误")
            bad += 1
            continue
        ds = cur["stars"] - e.get("snapshot_stars", 0)
        sign = f"{ds:+d}" if ds else "  0"
        pushed = (cur["pushed"] or "????-??-??")[:10]
        print(f"  [{cur['stars']:>6}★ {sign}] {repo}  (last_push {pushed})")
    if bad:
        print(f"\n✗ {bad} 条链接失效，请修复 registry.json 与 README")
        return 1
    print("\n✓ 全部链接有效")
    return 0


if __name__ == "__main__":
    sys.exit(main())
