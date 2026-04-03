# Storage Path Configuration Guide

## Overview

The `writing-workflow` skill supports flexible storage path configuration, allowing you to store writing projects in any directory you prefer.

## Configuration Methods

### Method 1: Conversation-Level (Highest Priority)

Specify the path directly in your conversation:

```text
"Store this project in ~/Documents/my-articles/"
"Use /Users/me/writing-projects/ as the base path"
"Save everything to ~/Dropbox/content/"
```

**Use when:**
- One-off projects with special storage needs
- Testing different storage locations
- Temporary projects

### Method 2: Settings Configuration (Persistent)

Add to `.claude/settings.json`:

```json
{
  "writing-workflow": {
    "base_path": "/Users/username/Documents/writing-projects"
  }
}
```

**Use when:**
- You want all projects in the same location
- Setting up a permanent writing workspace
- Sharing configuration across sessions

### Method 3: Default Fallback

If no configuration exists, uses:
```text
content-projects/
```
(relative to current working directory)

## Path Resolution Examples

### Example 1: User Instruction
```text
User: "Write an article about AI, store it in ~/articles/"
Resolved: /Users/username/articles/ai-article-slug/
```

### Example 2: Settings Configuration
```json
// .claude/settings.json
{
  "writing-workflow": {
    "base_path": "~/Documents/writing"
  }
}
```
```text
User: "Write an article about AI"
Resolved: /Users/username/Documents/writing/ai-article-slug/
```

### Example 3: Default
```text
User: "Write an article about AI"
Current directory: /Users/username/projects/
Resolved: /Users/username/projects/content-projects/ai-article-slug/
```

## Path Normalization

The skill automatically:
- Expands `~` to your home directory
- Converts relative paths to absolute paths
- Removes trailing slashes
- Creates parent directories if needed

## Project Structure

Regardless of base path, each project follows this structure:

```text
{base_path}/{project-slug}/
├── brief/
│   └── brief.md
├── research/
│   ├── research-2026-04-03.md
│   └── research-outline-2026-04-03.md
├── drafting/
│   ├── draft-zh.md
│   └── draft-en.md
├── polish/
│   ├── review-notes.md
│   ├── humanized-zh.md
│   └── humanized-en.md
├── assets/
│   ├── images/
│   └── image-prompts/
├── distribution/
│   ├── wechat-article.md
│   ├── seo-blog-zh.md
│   └── xiaohongshu-post.md
└── meta/
    ├── retrospective.md
    └── project-history.yaml
```

## Common Use Cases

### Use Case 1: Obsidian Vault Integration
```json
{
  "writing-workflow": {
    "base_path": "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/writing-projects"
  }
}
```

### Use Case 2: Dropbox Sync
```json
{
  "writing-workflow": {
    "base_path": "~/Dropbox/content-production"
  }
}
```

### Use Case 3: Project-Specific Storage
```text
User: "For this WeChat series, store everything in ~/wechat-2026-q2/"
```

## Troubleshooting

### Path not found
- Ensure parent directory exists
- Check for typos in path
- Verify permissions

### Settings not loading
- Check `.claude/settings.json` syntax
- Ensure proper JSON formatting
- Restart Claude Code session

### Path conflicts
- Conversation instruction overrides settings
- Settings override default
- Check which path is actually being used

## Best Practices

1. **Use absolute paths in settings** - more reliable than relative paths
2. **Use `~` for portability** - works across different machines
3. **Keep base path consistent** - easier to find projects later
4. **Document your choice** - add a comment in settings.json explaining why
5. **Backup regularly** - especially if using cloud sync

## Migration Guide

### Moving existing projects

If you have projects in `content-projects/` and want to move them:

```bash
# Option 1: Move all projects
mv content-projects/* ~/Documents/writing-projects/

# Option 2: Update settings to point to existing location
# Edit .claude/settings.json to use current location
```

### Updating settings

```bash
# Edit settings
code .claude/settings.json

# Add configuration
{
  "writing-workflow": {
    "base_path": "/your/preferred/path"
  }
}
```

## FAQ

**Q: Can I use different paths for different projects?**  
A: Yes, specify the path in conversation for each project.

**Q: What happens if I change the base path mid-project?**  
A: The skill resolves path at project start. Changing settings won't affect ongoing projects.

**Q: Can I use environment variables?**  
A: Not directly. Use absolute paths or `~` for home directory.

**Q: Does this work with sub-skills?**  
A: Yes, all sub-skills (content-briefing, content-research, etc.) use the resolved path.

**Q: Can I see which path is being used?**  
A: The skill announces the resolved path when starting a new project.
