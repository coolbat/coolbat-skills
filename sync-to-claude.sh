#!/usr/bin/env bash
# sync-to-claude.sh
# 将 coolbat-skills/skills/ 下的自有 skills 同步为 ~/.claude/skills/ 的符号链接
# 唯一真相源：/Users/coolbat/coolbat-skills/skills/

set -euo pipefail

REPO_SKILLS_DIR="/Users/coolbat/coolbat-skills/skills"
CLAUDE_SKILLS_DIR="/Users/coolbat/.claude/skills"
BACKUP_DIR="/Users/coolbat/.claude/skills-backup-$(date +%Y%m%d_%H%M%S)"

# 需要管理的自有 skills（第三方 skills 不在此列表中）
OWN_SKILLS=(
  writing-workflow
  content-briefing
  content-research
  content-drafting
  content-polishing
  content-humanizing
  content-repurpose
  content-style-learning
  content-topic-selection
  product-thinking-router
  premium-tool-page
  stitch-design-brief
)

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_ok()   { echo -e "${GREEN}[OK]${NC}    $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC}  $1"; }
log_err()  { echo -e "${RED}[ERROR]${NC} $1"; }
log_info() { echo "        $1"; }

# 检查源目录
if [ ! -d "$REPO_SKILLS_DIR" ]; then
  log_err "源目录不存在: $REPO_SKILLS_DIR"
  exit 1
fi

if [ ! -d "$CLAUDE_SKILLS_DIR" ]; then
  log_err "Claude skills 目录不存在: $CLAUDE_SKILLS_DIR"
  exit 1
fi

echo "=== coolbat-skills 同步脚本 ==="
echo "源目录:   $REPO_SKILLS_DIR"
echo "目标目录: $CLAUDE_SKILLS_DIR"
echo ""

# 检查哪些 skills 需要同步
NEEDS_SYNC=()
ALREADY_SYNCED=()
MISSING_SOURCE=()

for skill in "${OWN_SKILLS[@]}"; do
  src="$REPO_SKILLS_DIR/$skill"
  dst="$CLAUDE_SKILLS_DIR/$skill"

  if [ ! -d "$src" ]; then
    MISSING_SOURCE+=("$skill")
    continue
  fi

  if [ -L "$dst" ]; then
    current_target=$(readlink "$dst")
    if [ "$current_target" = "$src" ]; then
      ALREADY_SYNCED+=("$skill")
    else
      NEEDS_SYNC+=("$skill")
    fi
  else
    NEEDS_SYNC+=("$skill")
  fi
done

# 报告状态
echo "--- 状态检查 ---"
for skill in "${ALREADY_SYNCED[@]+"${ALREADY_SYNCED[@]}"}"; do
  log_ok "已同步: $skill"
done
for skill in "${NEEDS_SYNC[@]+"${NEEDS_SYNC[@]}"}"; do
  log_warn "需要同步: $skill"
done
for skill in "${MISSING_SOURCE[@]+"${MISSING_SOURCE[@]}"}"; do
  log_err "源目录缺失: $skill"
done
echo ""

# 如果没有需要同步的，直接退出
if [ ${#NEEDS_SYNC[@]} -eq 0 ]; then
  echo "所有 skills 已是最新状态，无需同步。"
  exit 0
fi

# 创建备份（仅备份需要替换的）
echo "--- 创建备份 ---"
mkdir -p "$BACKUP_DIR"
for skill in "${NEEDS_SYNC[@]}"; do
  dst="$CLAUDE_SKILLS_DIR/$skill"
  if [ -e "$dst" ]; then
    cp -R "$dst" "$BACKUP_DIR/"
    log_info "已备份: $skill -> $BACKUP_DIR/"
  fi
done
echo ""

# 执行同步
echo "--- 创建符号链接 ---"
SYNCED_COUNT=0
FAILED_COUNT=0

for skill in "${NEEDS_SYNC[@]}"; do
  src="$REPO_SKILLS_DIR/$skill"
  dst="$CLAUDE_SKILLS_DIR/$skill"

  # 删除旧的（符号链接或目录）
  rm -rf "$dst"

  # 创建新符号链接
  if ln -s "$src" "$dst"; then
    log_ok "已创建: $skill -> $src"
    ((SYNCED_COUNT++)) || true
  else
    log_err "创建失败: $skill"
    ((FAILED_COUNT++)) || true
  fi
done
echo ""

# 验证
echo "--- 验证结果 ---"
VALID_COUNT=0
BROKEN_COUNT=0

for skill in "${OWN_SKILLS[@]}"; do
  dst="$CLAUDE_SKILLS_DIR/$skill"
  src="$REPO_SKILLS_DIR/$skill"

  if [ ! -d "$src" ]; then
    continue
  fi

  if [ -L "$dst" ] && [ -d "$dst" ]; then
    log_ok "$skill"
    ((VALID_COUNT++)) || true
  else
    log_err "验证失败: $skill"
    ((BROKEN_COUNT++)) || true
  fi
done
echo ""

# 汇总
echo "=== 同步完成 ==="
echo "新建符号链接: $SYNCED_COUNT"
echo "验证通过:     $VALID_COUNT"
if [ $BROKEN_COUNT -gt 0 ]; then
  log_err "验证失败: $BROKEN_COUNT"
fi
if [ -d "$BACKUP_DIR" ] && [ "$(ls -A $BACKUP_DIR)" ]; then
  echo "备份位置:     $BACKUP_DIR"
fi
echo ""
echo "回滚方法："
echo "  rm -rf /Users/coolbat/.claude/skills/{$(IFS=,; echo "${OWN_SKILLS[*]}")}"
echo "  cp -R $BACKUP_DIR/* /Users/coolbat/.claude/skills/"
