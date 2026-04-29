#!/usr/bin/env bash

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
GITHUB_REPO="https://github.com/coolbat/coolbat-skills.git"
SKILLS_DIR="$HOME/.claude/skills"
TEMP_DIR="/tmp/coolbat-skills-install-$$"

# Sub-skills required by writing-workflow
REQUIRED_SKILLS=(
    "content-briefing"
    "content-research"
    "content-drafting"
    "content-polishing"
    "content-humanizing"
    "content-repurpose"
    "content-style-learning"
    "content-topic-selection"
)

# Flags
DRY_RUN=false
VERBOSE=false

# Helper functions
info()    { echo -e "${BLUE}[info]${NC}  $*"; }
success() { echo -e "${GREEN}[ok]${NC}    $*"; }
warn()    { echo -e "${YELLOW}[warn]${NC}  $*"; }
error()   { echo -e "${RED}[error]${NC} $*" >&2; }
step()    { echo -e "\n${BLUE}==>${NC} $*"; }

die() {
    error "$*"
    exit 1
}

usage() {
    cat <<EOF
Usage: install.sh [OPTIONS]

Installs writing-workflow and all required sub-skills into ~/.claude/skills/

Options:
  --dry-run     Show what would be installed without making any changes
  --help        Show this help message

Examples:
  # Quick install via curl:
  curl -sSL https://raw.githubusercontent.com/coolbat/coolbat-skills/main/skills/writing-workflow/install.sh | bash

  # Local install from repo:
  ./install.sh

  # Preview what would happen:
  ./install.sh --dry-run
EOF
}

# Parse arguments
for arg in "$@"; do
    case "$arg" in
        --dry-run) DRY_RUN=true ;;
        --help|-h) usage; exit 0 ;;
        *) die "Unknown option: $arg. Run with --help for usage." ;;
    esac
done

# Detect if we're running from a local clone or via curl
detect_source() {
    # BASH_SOURCE[0] is the script path; if it's /dev/stdin we're piped from curl
    local script_path="${BASH_SOURCE[0]:-}"
    if [[ -z "$script_path" || "$script_path" == "/dev/stdin" || "$script_path" == "bash" ]]; then
        echo "remote"
    else
        local script_dir
        script_dir="$(cd "$(dirname "$script_path")" && pwd)"
        # Check if the skills directory is two levels up (skills/writing-workflow/install.sh)
        local candidate_skills_dir
        candidate_skills_dir="$(dirname "$script_dir")"
        if [[ -d "$candidate_skills_dir/content-briefing" ]]; then
            echo "local:$candidate_skills_dir"
        else
            echo "remote"
        fi
    fi
}

# Check for required tools
check_deps() {
    local missing=()
    for cmd in git cp mkdir; do
        command -v "$cmd" &>/dev/null || missing+=("$cmd")
    done
    if [[ ${#missing[@]} -gt 0 ]]; then
        die "Missing required tools: ${missing[*]}"
    fi
}

# Ensure target skills directory exists
ensure_skills_dir() {
    if [[ "$DRY_RUN" == true ]]; then
        info "[dry-run] Would create directory: $SKILLS_DIR"
        return
    fi
    if [[ ! -d "$SKILLS_DIR" ]]; then
        warn "Skills directory not found: $SKILLS_DIR"
        read -r -p "Create it now? [y/N] " answer
        case "$answer" in
            [yY]*) mkdir -p "$SKILLS_DIR"; success "Created $SKILLS_DIR" ;;
            *) die "Aborted. Install $SKILLS_DIR manually and re-run." ;;
        esac
    fi
}

# Clone repo to temp dir for remote installs
fetch_remote() {
    step "Fetching skills from GitHub..."
    if [[ "$DRY_RUN" == true ]]; then
        info "[dry-run] Would clone $GITHUB_REPO to $TEMP_DIR"
        echo "$TEMP_DIR"
        return
    fi
    if ! git clone --depth=1 --quiet "$GITHUB_REPO" "$TEMP_DIR" 2>&1; then
        die "Failed to clone $GITHUB_REPO. Check your internet connection."
    fi
    success "Repository fetched."
    echo "$TEMP_DIR"
}

# Install a single skill from a source directory
install_skill() {
    local skill="$1"
    local source_skills_dir="$2"
    local src="$source_skills_dir/$skill"
    local dst="$SKILLS_DIR/$skill"

    if [[ ! -d "$src" ]]; then
        warn "Source not found for skill: $skill (expected at $src)"
        return 1
    fi

    if [[ -d "$dst" ]]; then
        info "Already installed, skipping: $skill"
        return 0
    fi

    if [[ "$DRY_RUN" == true ]]; then
        info "[dry-run] Would install: $skill -> $dst"
        return 0
    fi

    cp -r "$src" "$dst"
    success "Installed: $skill"
}

# Install writing-workflow itself
install_main_skill() {
    local source_skills_dir="$1"
    install_skill "writing-workflow" "$source_skills_dir"
}

# Verify all skills are present after install
verify_install() {
    step "Verifying installation..."
    local all_skills=("writing-workflow" "${REQUIRED_SKILLS[@]}")
    local failed=()

    for skill in "${all_skills[@]}"; do
        if [[ "$DRY_RUN" == true ]]; then
            info "[dry-run] Would verify: $SKILLS_DIR/$skill"
        elif [[ -d "$SKILLS_DIR/$skill" ]]; then
            success "Found: $skill"
        else
            error "Missing: $skill"
            failed+=("$skill")
        fi
    done

    if [[ ${#failed[@]} -gt 0 ]]; then
        echo ""
        error "Installation incomplete. Missing skills: ${failed[*]}"
        return 1
    fi
}

# Cleanup temp dir on exit
cleanup() {
    if [[ -d "$TEMP_DIR" ]]; then
        rm -rf "$TEMP_DIR"
    fi
}
trap cleanup EXIT

# ─── Main ────────────────────────────────────────────────────────────────────

main() {
    echo ""
    echo -e "${BLUE}writing-workflow installer${NC}"
    echo "─────────────────────────────────────────"
    if [[ "$DRY_RUN" == true ]]; then
        warn "Dry-run mode: no changes will be made."
    fi

    check_deps
    ensure_skills_dir

    local source
    source="$(detect_source)"

    local source_skills_dir
    if [[ "$source" == remote ]]; then
        source_skills_dir="$(fetch_remote)/skills"
    else
        source_skills_dir="${source#local:}"
        step "Using local source: $source_skills_dir"
    fi

    step "Installing sub-skills..."
    local failed_skills=()
    for skill in "${REQUIRED_SKILLS[@]}"; do
        install_skill "$skill" "$source_skills_dir" || failed_skills+=("$skill")
    done

    step "Installing writing-workflow..."
    install_main_skill "$source_skills_dir" || failed_skills+=("writing-workflow")

    if [[ ${#failed_skills[@]} -gt 0 ]]; then
        echo ""
        warn "Some skills could not be installed: ${failed_skills[*]}"
    fi

    verify_install

    echo ""
    if [[ "$DRY_RUN" == true ]]; then
        success "Dry-run complete. Re-run without --dry-run to apply."
    else
        success "All done. Start with /writing-workflow in Claude Code."
    fi
    echo ""
}

main "$@"
