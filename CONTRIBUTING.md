# 🤝 Contributing Guidelines

Want to improve this repo? Great! Here's how.

---

## What to Contribute

### 📚 Add New Badge Guides

If we're missing a badge, add it:

1. Create folder: `/badges/BADGE_NAME/`
2. Add `GENIUS.md` — Legitimate methods
3. Add `HACK.md` — Creative exploits (with warnings)
4. Include examples and timelines

**Template:**

```markdown
# 🎯 BADGE NAME — GENIUS/HACK METHODS

**Goal:** [What the badge requires]

---

## Method 1: [Approach]

[Detailed explanation]

[Code examples if applicable]

**Result:** [What you get]
**Time:** [How long it takes]
**Risk:** [If applicable]
```

### 🛠️ Add Tools

Tools should:
- Be practical and testable
- Include clear usage examples
- Solve a real problem
- Have error handling
- Be documented

**Submit as:**
```
/tools/tool-name.py (or .js)
```

Include header comment with:
```python
#!/usr/bin/env python3
"""
Tool name and description
Usage: python3 tool-name.py --arg value
Requirements: requests, github
"""
```

### 📖 Improve Documentation

- Fix typos
- Clarify confusing sections
- Add more examples
- Update outdated info
- Better formatting

### ✅ Add Checklists/Templates

If you have a useful checklist or template for earning badges, add it to:
```
/guides/your-guide.md
```

---

## How to Contribute

### Step 1: Fork the Repo

```bash
# Fork on GitHub (click Fork button)
# Then clone your fork
git clone https://github.com/YOUR-USERNAME/github-badges-hack-genius.git
cd github-badges-hack-genius
```

### Step 2: Create a Branch

```bash
# Create feature branch
git checkout -b add/quickdraw-guide
# or
git checkout -b fix/typo-in-readme
# or
git checkout -b improve/pull-shark-examples
```

### Step 3: Make Changes

- Edit files
- Add new files
- Test if applicable
- Keep formatting consistent

### Step 4: Commit

```bash
git add .
git commit -m "Add: Quickdraw detailed guide with examples"
```

**Commit message format:**
```
Add: New feature/guide
Fix: Bug fix
Improve: Enhancement to existing content
Update: Refresh outdated info
Docs: Documentation improvement
```

### Step 5: Push

```bash
git push origin add/quickdraw-guide
```

### Step 6: Create Pull Request

1. Go to GitHub repo
2. Click "Compare & pull request"
3. Fill in PR description
4. Reference issue if applicable
5. Submit!

---

## Content Guidelines

### For GENIUS.md Files

✅ **Do:**
- Provide realistic timelines
- Include concrete examples
- Link to resources
- Explain the "why" not just "how"
- Be encouraging but honest

❌ **Don't:**
- Over-promise speed
- Omit effort required
- Provide insufficient examples
- Make it sound easy when it's hard

### For HACK.md Files

✅ **Do:**
- Clearly mark risk levels
- Explain ToS implications
- Test code before submitting
- Explain why it works
- Include warnings

❌ **Don't:**
- Encourage ToS violations
- Omit risks
- Provide untested code
- Make hacks sound safer than they are

### For Tools

✅ **Do:**
- Include docstrings
- Handle errors gracefully
- Provide usage examples
- Test on Python 3.8+
- Be idempotent where possible

❌ **Don't:**
- Require unseen dependencies
- Ignore errors
- Leave TODOs incomplete
- Be OS-specific without notice

---

## Quality Checklist

Before submitting PR:

- [ ] Grammar & spelling checked
- [ ] Links work
- [ ] Code is tested
- [ ] Examples are accurate
- [ ] Formatting is consistent
- [ ] Risk levels are clear
- [ ] No personally identifiable info
- [ ] References to other sections are correct

---

## Code Style

### Python
```python
#!/usr/bin/env python3
"""Module docstring"""

def function_name(param: str) -> int:
    """Function docstring"""
    return 42
```

### JavaScript
```javascript
/**
 * Function description
 * @param {string} param - Parameter description
 * @returns {number} Return description
 */
function functionName(param) {
  return 42;
}
```

### Markdown
```markdown
# Heading 1

## Heading 2

### Heading 3

**Bold** *italic* `code`

- List item
- Another item

1. Numbered
2. Item

[Link](url)
```

---

## Reporting Issues

See a problem? Report it:

1. Check if issue already exists
2. Create new issue with:
   - **Title:** Clear, specific
   - **Description:** What's wrong
   - **Example:** Show the problem
   - **Suggestion:** How to fix (if you have one)

---

## Large Contributions

For significant changes:

1. **Open issue first** to discuss
2. **Get feedback** from maintainer
3. **Make changes** in feature branch
4. **Submit PR** referencing issue
5. **Respond to feedback** promptly

---

## Recognition

Contributors who submit useful additions will be:
- Listed in README
- Credited in relevant sections
- Given credit in commit messages

---

## Questions?

- Open an issue
- Email maintainer
- Check existing PRs/issues
- Read relevant guides

---

## License

By contributing, you agree that your contributions are licensed under the same license as the project (MIT).

---

**Thank you for contributing! 🙏**

Every improvement makes this resource better for the whole community.
