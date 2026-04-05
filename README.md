# GitHub Badges: Hack vs Genius Edition 🏆

A comprehensive guide to earning GitHub achievements—both the legitimate (genius) way and the creative (hack) way.

> **Disclaimer:** This repo is for educational purposes. Hack methods may violate GitHub ToS. Use at your own risk. Always prefer genius methods for real profiles.

---

## 📋 Table of Contents

- [Repo Structure](#repo-structure)
- [Badge Categories](#badge-categories)
- [Quick Start](#quick-start)
- [How to Use This Repo](#how-to-use-this-repo)
- [Contributing](#contributing)

---

## 🗂️ Repo Structure

```
github-badges-hack-genius/
├── README.md                          # This file
├── QUICK_START.md                     # Fast track to badge earning
├── GENIUS_METHODS.md                  # Legitimate ways (recommended)
├── HACK_METHODS.md                    # Creative exploits (educational)
├── badges/
│   ├── pull-shark/
│   │   ├── GENIUS.md
│   │   ├── HACK.md
│   │   └── tools/
│   ├── starstruck/
│   │   ├── GENIUS.md
│   │   ├── HACK.md
│   │   └── tools/
│   ├── galaxy-brain/
│   ├── quickdraw/
│   ├── pair-extraordinaire/
│   ├── yolo/
│   ├── sponsor/
│   └── arctic-code-vault/              # Historical (not earnable)
├── tools/
│   ├── badge-tracker.py               # Track progress toward badges
│   ├── pr-automation.js                # Auto-create PRs for testing
│   └── discussion-monitor.py           # Monitor discussions for answers
├── guides/
│   ├── github-api-tricks.md            # API-based workarounds
│   ├── automation-setup.md             # Bot/workflow setup
│   └── community-strategy.md           # Social approach
└── CONTRIBUTING.md
```

---

## 🎯 Badge Categories

### Tier 1: Easy (Single Merge/Action)

| Badge | Variants | Genius | Hack | Difficulty |
|-------|----------|--------|------|------------|
| **YOLO** | None | Merge PR without review in own repo | Self-merge instantly in empty repo | ⭐ |
| **Quickdraw** | None | Merge PR <5min after opening | Merge in own repo immediately | ⭐ |
| **Sponsor** | None | Pay $1+ to GitHub Sponsors | Use alt account to sponsor yourself (TOS violation) | ⭐⭐ |

### Tier 2: Medium (Effort-Based)

| Badge | Variants | Genius | Hack | Difficulty |
|-------|----------|--------|------|------------|
| **Pull Shark** | Bronze, Silver, Gold | Contribute to open-source, get PRs merged | Generate fake commits, merge in bulk | ⭐⭐ |
| **Pair Extraordinaire** | Bronze, Silver, Gold | Co-author commits with real collaborators | Use co-author syntax in your own commits | ⭐⭐⭐ |
| **Galaxy Brain** | Bronze, Silver, Gold | Answer discussions helpfully | Answer your own questions, get friend to mark as solved | ⭐⭐⭐ |

### Tier 3: Hard (Skill/Community)

| Badge | Variants | Genius | Hack | Difficulty |
|-------|----------|--------|------|------------|
| **Starstruck** | Bronze, Silver, Gold | Build an awesome project, promote it | Bot farm stars, exchange stars with friends | ⭐⭐⭐⭐ |

### Tier 4: Historical (Unobtainable)

- Arctic Code Vault Contributor
- Mars 2020 Contributor

---

## ⚙️ Setup

### Prerequisites

- Python 3.7+
- Git
- GitHub CLI (optional, for some automation)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd GitHub__Badge
   ```

2. **Create a virtual environment:**
   ```bash
   # On Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install requests
   ```

---

## 🚀 Quick Start

### For Genius Methods (Recommended)

1. **Start with YOLO & Quickdraw:** Create a simple repo, make quick PRs, merge them.
2. **Build Pull Shark:** Contribute to 5-10 beginner-friendly open-source repos.
3. **Answer Questions (Galaxy Brain):** Join active repos' discussions, solve real problems.
4. **Star-Hunt (Starstruck):** Build a useful tool and market it.

**Estimated time:** 2-6 weeks for bronze badges.

### For Hack Methods (Educational)

1. Review `HACK_METHODS.md` for workarounds and automation.
2. Check badge-specific guides in `/badges/*/HACK.md`.
3. Use tools in `/tools/` to automate processes.

---

## 📖 How to Use This Repo

### For Badge Hunters

```bash
# Clone repo
git clone https://github.com/Aashish-po/github-badges-hack-genius.git
cd github-badges-hack-genius

# Pick a badge category
cat badges/pull-shark/GENIUS.md      # Read legitimate approach
cat badges/pull-shark/HACK.md        # Understand workarounds

# Use tools for tracking
python3 tools/badge-tracker.py --user YOUR_USERNAME
```

### For Developers

1. Read `GENIUS_METHODS.md` for sustainable strategies.
2. Integrate provided tools into your workflow.
3. Contribute improvements back.

---

## 🔗 Badge Guides

Each badge has a dedicated folder with:

- **GENIUS.md** — Legitimate, sustainable methods
  - Real projects to contribute to
  - Community best practices
  - Realistic timelines
  - Skill development tips

- **HACK.md** — Creative exploits & automation
  - API tricks
  - Bot strategies
  - Workflow automation
  - ⚠️ **Risk level & ToS implications**

---

## 🛠️ Tools Included

### `badge-tracker.py`
Track progress toward badges with real-time API queries.

```bash
python3 tools/badge-tracker.py --user Aashish-po
```

### `pr-automation.js`
Auto-create and merge test PRs (for your own repos).

```bash
node tools/pr-automation.js --repo my-test-repo --count 5
```

### `discussion-monitor.py`
Monitor discussions and get notified of answerable questions.

```bash
python3 tools/discussion-monitor.py --repo kubernetes/kubernetes
```

---

## 📊 Badge Earning Chart

```
┌─────────────────┬──────────┬─────────┬──────────┐
│ Badge           │ Bronze   │ Silver  │ Gold     │
├─────────────────┼──────────┼─────────┼──────────┤
│ Pull Shark      │ 4 PRs    │ 16 PRs  │ 128 PRs  │
│ Starstruck      │ 16 ⭐    │ 128 ⭐  │ 512 ⭐   │
│ Galaxy Brain    │ 1 ans    │ 10 ans  │ 25 ans   │
│ Pair Extraord.  │ 1 commit │ 10 com  │ 24 com   │
└─────────────────┴──────────┴─────────┴──────────┘
```

---

## ⚠️ Risk Levels

### ✅ Safe (No ToS Risk)
- YOLO, Quickdraw in your own repos
- Legitimate PR contributions
- Real discussion answers
- GitHub Sponsors (legitimate)

### ⚠️ Medium Risk (ToS Gray Area)
- Automated PR generation in test repos
- Self-co-authoring (technically allowed, ethically questionable)
- Bot-farm alternatives

### 🚫 High Risk (ToS Violation)
- Fake stars via bot networks
- Spam discussions
- Account manipulation
- Cross-account sponsorship schemes

---

## 🤝 Contributing

To add badge guides, tools, or strategies:

1. Fork the repo
2. Add to relevant `/badges/*/` folder or `/tools/`
3. Follow existing format (GENIUS.md / HACK.md structure)
4. Submit PR with clear description

See `CONTRIBUTING.md` for details.

---

## 📚 Resources

- [GitHub Achievements Docs](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/personalizing-your-profile#displaying-badges-on-your-profile)
- [GitHub API Reference](https://docs.github.com/en/rest)
- [GitHub Discussions Guide](https://docs.github.com/en/discussions)

---

## 📝 License

MIT License — Use freely, credit appreciated.

---

## 👤 Author

Created by **@Aashish-po** | Fork & adapt for your own use.

---

**Remember:** Genius badges are achievements you can be proud of. Hack badges are fun to learn from, but use wisely. 🎓
# GitHub_Badge
# GitHub_Badge
