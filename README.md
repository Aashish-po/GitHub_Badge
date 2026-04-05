# GitHub Badges: Hack vs Genius Edition 🏆

<div align="center">
  <img src="Media/Misc/GitHub_Logo/pinned-octocat.svg" alt="GitHub Octocat" width="150">
</div>

A comprehensive guide to earning GitHub achievements—both the legitimate (genius) way and the creative (hack) way.

> **Disclaimer:** This repo is for educational purposes. Hack methods may violate GitHub ToS. Use at your own risk. Always prefer genius methods for real profiles.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Repo Structure](#repo-structure)
- [Quick Start](#quick-start)
- [Badge Categories](#badge-categories)
- [Setup](#setup)
- [How to Use](#how-to-use-this-repo)
- [Tools & Resources](#tools-included)
- [Risk Levels](#risk-levels)
- [GitHub Highlights](#github-highlights-special-badges)
- [Contributing](#contributing)
- [Resources](#resources)
- [License](#license)
- [Support & Community](#support--community)

---

## 🗂️ Repo Structure

```
GitHub__Badge/
├── README.md                          # Main documentation (this file)
├── LICENSE                            # MIT License
├── CHANGELOG.md                       # Version history and updates
├── CODE_OF_CONDUCT.md                 # Community guidelines
├── SECURITY.md                        # Security policy & vulnerability reporting
├── CONTRIBUTING.md                    # Contribution guidelines
├── QUICK_START.md                     # Fast track to badge earning (30-day plan)
├── GENIUS_METHODS.md                  # Legitimate ways (recommended)
├── HACK_METHODS.md                    # Creative exploits (educational)
├── badge-tracker.py                   # Track progress toward badges
├── setup.sh                           # Setup script for macOS/Linux
├── setup.bat                          # Setup script for Windows
├── Media/                             # Badge and highlight assets
│   ├── Badges/                        # Badge SVG/PNG files with docs
│   ├── Highlights/                    # Highlight badges (GitHub Pro, etc.)
│   └── Misc/                          # GitHub logos and emojis
├── .venv/                             # Virtual environment directory (auto-generated)
└── .gitignore                         # Git ignore configuration
```

---

## 🎯 Badge Categories

### Tier 1: Easy (Single Merge/Action)

| Badge | Variants | Genius | Hack | Difficulty |
|-------|----------|--------|------|------------|
| ![YOLO](Media/Badges/YOLO/PNG/YOLO_Badge.png) **YOLO** | None | Merge PR without review in own repo | Self-merge instantly in empty repo | ⭐ |
| ![Quick-Draw](Media/Badges/Quick-Draw/PNG/Skin-Tones/QuickDraw_SkinTone1.png) **Quickdraw** | None | Merge PR <5min after opening | Merge in own repo immediately | ⭐ |
| ![Sponsor](Media/Badges/GitHub-Sponsor/PNG/GitHubSponsorBadge.png) **Sponsor** | None | Pay $1+ to GitHub Sponsors | Use alt account to sponsor yourself (TOS violation) | ⭐⭐ |

### Tier 2: Medium (Effort-Based)

| Badge | Variants | Genius | Hack | Difficulty |
|-------|----------|--------|------|------------|
| ![Pull Shark](Media/Badges/Pull-Shark/PNG/PullShark.png) **Pull Shark** | Bronze, Silver, Gold | Contribute to open-source, get PRs merged | Generate fake commits, merge in bulk | ⭐⭐ |
| ![Pair Extraordinaire](Media/Badges/Pair-Extraordinaire/PNG/PairExtraordinaire.png) **Pair Extraordinaire** | Bronze, Silver, Gold | Co-author commits with real collaborators | Use co-author syntax in your own commits | ⭐⭐⭐ |
| ![Galaxy Brain](Media/Badges/Galaxy-Brain/PNG/GalaxyBrain.png) **Galaxy Brain** | Bronze, Silver, Gold | Answer discussions helpfully | Answer your own questions, get friend to mark as solved | ⭐⭐⭐ |

### Tier 3: Hard (Skill/Community)

| Badge | Variants | Genius | Hack | Difficulty |
|-------|----------|--------|------|------------|
| ![Star-Struck](Media/Badges/Star-Struck/PNG/StarStruck_Bronze.png) **Starstruck** | Bronze, Silver, Gold | Build an awesome project, promote it | Bot farm stars, exchange stars with friends | ⭐⭐⭐⭐ |

### Tier 4: Historical (Unobtainable)

- ![Arctic Code Vault](Media/Badges/2020-Arctic-Code-Vault-Contributor/PNG/2020ArcticCodeVaultBadge.png) **Arctic Code Vault Contributor**
- ![Mars 2020 Contributor](Media/Badges/Mars-2020-Contributor/PNG/Mars2020ContributorBadge.png) **Mars 2020 Contributor**

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

1. **Start with ![YOLO](Media/Badges/YOLO/PNG/YOLO_Badge.png) YOLO & ![Quickdraw](Media/Badges/Quick-Draw/PNG/Skin-Tones/QuickDraw_SkinTone1.png) Quickdraw:** Create a simple repo, make quick PRs, merge them.
2. **Build ![Pull Shark](Media/Badges/Pull-Shark/PNG/PullShark.png) Pull Shark:** Contribute to 5-10 beginner-friendly open-source repos.
3. **Answer Questions (![Galaxy Brain](Media/Badges/Galaxy-Brain/PNG/GalaxyBrain.png) Galaxy Brain):** Join active repos' discussions, solve real problems.
4. **Star-Hunt (![Starstruck](Media/Badges/Star-Struck/PNG/StarStruck_Bronze.png) Starstruck):** Build a useful tool and market it.

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
│ Starstruck      │ 16       │ 128     │ 512      │
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

## 🌟 GitHub Highlights (Special Badges)

Beyond regular badges, GitHub also offers **Highlights** that display on your profile:

<div align="center">

**🔒 Security Achievements**

| Security Bug Bounty Hunter | Security Advisory Credit |
|:---:|:---:|
| ![Security Bug Bounty](Media/Highlights/Security-Bug-Bounty-Hunter/SVG/Security-Bug-Bounty-Hunter_LightMode.svg) | ![Security Advisory](Media/Highlights/Security-Advisory-Credit/SVG/Security-Advisory-Credit_LightMode.svg) |

**💻 Developer Programs**

| GitHub Pro | GitHub Campus Expert | Developer Program Member |
|:---:|:---:|:---:|
| ![Pro](Media/Highlights/GitHub-Pro/SVG/GitHub-Pro_LightMode.svg) | ![Campus](Media/Highlights/GitHub-Campus-Expert/SVG/GitHub-Campus-Expert_LightMode.svg) | ![Developer](Media/Highlights/Developer-Program-Member/SVG/DeveloperProgramMember_LightMode.svg) |

</div>

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

MIT License © 2024 GitHub__Badge Contributors

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

**You are free to:**
- ✅ Use commercially
- ✅ Modify the source
- ✅ Distribute copies
- ✅ Use privately

**You must:**
- ✅ Include license and copyright notice
- ✅ State changes made

---

## Support & Community

### Get Help

- 📖 **Documentation:** Read guides in this repo
- 💬 **Discussions:** Open GitHub Discussions
- 🐛 **Bug Reports:** [Create an issue](https://github.com/Aashish-po/GitHub__Badge/issues)
- 🔒 **Security Issues:** See [SECURITY.md](SECURITY.md)

### Code of Conduct

We have a [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and inclusive community.

### Version History

See [CHANGELOG.md](CHANGELOG.md) for:
- Version history
- Feature updates
- Breaking changes
- Deprecations

### Contributors

This project is maintained by [@Aashish-po](https://github.com/Aashish-po) and the community.

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 👤 Author & Attribution

**Created by:** [@Aashish-po](https://github.com/Aashish-po)  
**License:** MIT  
**Last Updated:** April 5, 2024

Fork & adapt for your own use. ⭐ Star if helpful!

---

**Remember:** Genius badges are achievements you can be proud of. Hack badges are fun to learn from, but use wisely. 🎓
# GitHub_Badge
# GitHub_Badge
