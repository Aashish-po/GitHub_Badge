# ⚡ GitHub Badges: 30-Day Quick Start

<div align="center">
  <img src="Media/Misc/GitHub_Logo/pinned-octocat.svg" alt="GitHub" width="150">
</div>

**Can you get badges in 30 days? Yes. Here's how.**

---

## 🔧 Setup First

Before starting, set up your environment:

```bash
# Clone the repo
git clone <repo-url>
cd GitHub__Badge

# Create virtual environment
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install requests
```

---

## 🎯 Realistic 30-Day Goals

| Badge | Goal | Achievable? |
|-------|------|------------|
| ![YOLO](Media/Badges/YOLO/PNG/YOLO_Badge.png) **YOLO** | 1 | ✅ Day 1 |
| ![Quickdraw](Media/Badges/Quick-Draw/PNG/Skin-Tones/QuickDraw_SkinTone1.png) **Quickdraw** | 1 | ✅ Day 1 |
| ![Pull Shark](Media/Badges/Pull-Shark/PNG/PullShark.png) **Pull Shark Bronze** | 4 PRs | ✅ Day 30 |
| ![Sponsor](Media/Badges/GitHub-Sponsor/PNG/GitHubSponsorBadge.png) **Sponsor** | 1 | ✅ Day 1 ($1) |
| ![Galaxy Brain](Media/Badges/Galaxy-Brain/PNG/GalaxyBrain.png) **Galaxy Brain Bronze** | 1 answer | ⚠️ Possible |
| ![Starstruck](Media/Badges/Star-Struck/PNG/StarStruck_Bronze.png) **Starstruck Bronze** | 16 stars | ⚠️ Unlikely (needs 1 great project) |

**Realistic 30-day result:** 3-4 badges minimum, with effort.

---

## 📅 Day-by-Day Schedule

### WEEK 1: Get Easy Badges

#### Day 1 (Monday)

**Goal:** Get ![YOLO](Media/Badges/YOLO/PNG/YOLO_Badge.png) YOLO + ![Quickdraw](Media/Badges/Quick-Draw/PNG/Skin-Tones/QuickDraw_SkinTone1.png) Quickdraw

```bash
# Create test repo
mkdir github-badges-test
cd github-badges-test
git init
echo "# Test" > README.md
git add .
git commit -m "Init"
git push -u origin main

# Create a branch & PR
git checkout -b yolo-test
echo "YOLO!" >> README.md
git commit -am "YOLO update"
git push origin yolo-test

# Create PR (requires GitHub CLI)
gh pr create --title "YOLO test" --body "This is a test PR"

# Get PR number from output, then merge
gh pr merge <PR_NUMBER> --merge

# Back to main
git checkout main

# Create another branch & PR for Quickdraw
git checkout -b quickdraw-test
echo "Quickdraw test" >> README.md
git commit -am "Quickdraw update"
git push origin quickdraw-test
gh pr create --title "Quickdraw test" --body "Test"

# Immediately merge (within 5 minutes!)
gh pr merge <PR_NUMBER> --merge
```

✅ **Result:** YOLO + Quickdraw badges unlocked!

#### Day 2 (Tuesday)

**Goal:** Start ![Pull Shark](Media/Badges/Pull-Shark/PNG/PullShark.png) Pull Shark

- Find first "good first issue"
- Fork the repo
- Set up environment
- Start working on issue

**Search for issues:**
```bash
# Open GitHub, search:
is:open is:issue label:good-first-issue language:python
# (or your language)
```

#### Day 3-7 (Wed-Sun)

**Goal:** Submit 2-3 real PRs

- Complete Day 2 work → Submit PR
- Find new good-first-issue → Work on it
- Monitor feedback on PRs

**Expected:** 1-2 PRs merged by end of week

---

### WEEK 2-3: Build for ![Starstruck](Media/Badges/Star-Struck/PNG/StarStruck_Bronze.png) Starstruck

**Parallel to PRs:** Build a simple project

#### Day 8-14 (Week 2)

**Option A: Simple Tool**

```javascript
// star-tracker/index.js
const fetch = require('node-fetch');

async function getGitHubUser(username) {
  const res = await fetch(`https://api.github.com/users/${username}`);
  const data = await res.json();
  
  return {
    name: data.name,
    stars: data.public_repos,
    followers: data.followers,
  };
}

module.exports = { getGitHubUser };
```

**Create repo:** `github-star-tracker`
- Add to npm registry
- Write README
- Push to GitHub

#### Day 15-21 (Week 3)

**Launch:** Promote on social media

```bash
# Share on Twitter/LinkedIn
"Just released github-star-tracker! A tool to track your GitHub stars across all repos. Open source. Check it out: github.com/yourname/github-star-tracker"

# Post on relevant Discord
# Share in dev communities
# Add to awesome-tools list
```

**Expected:** 10-20 stars from launch

---

### WEEK 4: Polish & Contributions

#### Day 22-28

**Continue with PRs:**
- Submit 3-5 more PRs across different projects
- Maintain communication with reviewers
- Try to get them merged

**If your project is doing well:**
- Add new features
- Improve docs
- Respond to issues

**Target:** 4-8 more merged PRs = **Pull Shark Bronze!**

#### Day 29-30

**Consolidate:**
- Check badges earned
- Submit last PR attempts
- Plan month 2 strategy

---

## 🎁 Optimized Badge Path (30 Days)

### Best Case Scenario

```
Day 1:    YOLO ✅ + Quickdraw ✅ (2 badges)
Day 5:    First PR merged (1/4 for Pull Shark)
Day 10:   2 more PRs merged (3/4)
Day 15:   Pull Shark Bronze ✅ (1 more merged)
Day 20:   Good project gets 16 stars ✅ Starstruck Bronze
Day 30:   Galaxy Brain Bronze possible

Total: 5 badges in 30 days
```

### Realistic Scenario

```
Day 1:    YOLO ✅ + Quickdraw ✅
Day 10:   1 PR merged
Day 20:   2 more PRs merged (3 total)
Day 30:   Working on 4th PR (might merge next week)

Total: 2-3 badges, +3-4 PRs toward silver
```

---

## 🔥 How to Speed It Up

### Speed Hack 1: Work on Multiple Projects

Instead of 4 PRs to 1 repo, do:
- 1 PR to repo A
- 1 PR to repo B
- 1 PR to repo C
- 1 PR to repo D

Reason: Each project has different review cycles. While waiting for repo A, work on B.

### Speed Hack 2: Pick the Right Projects

Fast-merging projects:
- `awesome-*` lists (merge in hours)
- Beginner tutorials (they want contributors)
- `first-timers-only` projects (merge in days)

Slow projects:
- Major frameworks (weeks for review)
- Big companies (bureaucratic)
- Inactive repos (no reviews)

### Speed Hack 3: Pick the Right Issues

Quick-to-merge issues:
- Documentation fixes
- Typo corrections
- Example additions
- Test additions

Slow-to-merge issues:
- New features
- Breaking changes
- Performance optimization (needs benchmarks)
- API changes

### Speed Hack 4: Build Your Own Repo

If you make a repo yourself:
- You control merge timeline
- You can merge your own PRs
- Your own project = natural stars

---

## ✅ 30-Day Checklist

### Week 1
- [ ] Create test repo
- [ ] Merge YOLO PR
- [ ] Merge Quickdraw PR
- [ ] Find 3 good-first-issues

### Week 2
- [ ] Submit 2 real PRs
- [ ] Start building your project
- [ ] Write project README

### Week 3
- [ ] 1 more PR merged (3 total)
- [ ] Launch your project
- [ ] Promote on social media
- [ ] Get 10+ stars

### Week 4
- [ ] 1 more PR merged (4 total) = **BRONZE** ✅
- [ ] Gain 5+ more stars on project
- [ ] Plan next month goals

---

## 🚀 Tools You'll Need

```bash
# Install GitHub CLI
curl https://cli.github.com/install.sh | bash

# Or on Mac
brew install gh

# Or on Windows
choco install gh

# Verify
gh --version

# Authenticate
gh auth login
# (Choose HTTPS, then GitHub.com, then create token)
```

---

## 🎯 Key Insights for Speed

1. **Easy badges first** (YOLO, Quickdraw) = momentum
2. **Right project matters** (find fast-merging ones)
3. **Self-merge counts** (your own repo is fastest)
4. **Parallel tracks** (PRs + your own project together)
5. **Quality over speed** (one merged PR > 5 rejected)

---

## 📊 Stats

**Average developer:** 4 PRs = 3-4 weeks  
**You (optimized):** 4 PRs = 2-3 weeks  
**With own repo:** 4 PRs + Starstruck = 3-4 weeks  

---

## 🎓 Expected Learning

**By Day 30, you'll know:**
- How to fork/PR workflow
- GitHub API basics (gh CLI)
- How to write good commits
- Open source community norms
- What makes projects popular

Worth way more than badges alone!

---

## 🔗 Resources You'll Use

**Finding Issues:**
- https://firsttimersonly.com
- https://goodfirstissue.dev
- GitHub search: `is:open label:good-first-issue`

**Tools:**
- GitHub CLI: `gh`
- Git: `git`
- Text editor: VS Code

**Communities:**
- r/learnprogramming (Reddit)
- Dev.to
- GitHub Discussions

---

## 💪 Remember

**30 days is tight.** Be realistic:
- Focus on 1-2 badges maximum
- Build momentum with easy ones
- Enjoy the process of contributing
- Don't stress about unlocking everything

Even if you get just 1-2 badges, you'll have:
- Real contributions to real projects
- GitHub account with activity
- Proof of open source work
- Skills that matter way more than badges

**Let's go! 🚀**
