#!/usr/bin/env bash
# 打包 dme-skills 下各 skill 子目录为 <dir_name>.skill
# 用法: ./pack.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 检查 zip 是否可用
if ! command -v zip >/dev/null 2>&1; then
    echo "错误: 未找到 zip 命令，请先安装 zip（例如 apt install zip）" >&2
    exit 1
fi

packed=0
# */ 不匹配隐藏目录（自动排除 .git）
for dir in */; do
    [ -d "$dir" ] || continue
    name="${dir%/}"

    # 仅打包包含 SKILL.md 的 skill 目录
    [ -f "$name/SKILL.md" ] || continue

    out="$SCRIPT_DIR/$name.skill"
    rm -f "$out"

    # 打包目录内容，包内顶层即为 SKILL.md、references/ 等文件
    (
        cd "$name"
        shopt -s dotglob nullglob
        zip -qr "$out" *
    )

    echo "已生成: $name.skill ($(du -h "$out" | cut -f1))"
    packed=$((packed + 1))
done

if [ "$packed" -eq 0 ]; then
    echo "未找到任何 skill 子目录（需包含 SKILL.md）" >&2
    exit 1
fi

echo "完成，共打包 $packed 个 skill 包。"
