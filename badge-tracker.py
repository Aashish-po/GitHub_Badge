#!/usr/bin/env python3
"""
GitHub Badges Tracker
Track your progress toward GitHub achievement badges in real-time
"""

import requests

from typing import Dict, List, Tuple, Optional
from datetime import datetime


class GitHubBadgeTracker:
    """Track GitHub badges for a user"""

    BASE_URL = "https://api.github.com"

    # Badge thresholds
    BADGES = {
        "pull_shark": {
            "bronze": 4,
            "silver": 16,
            "gold": 128,
        },
        "starstruck": {
            "bronze": 16,
            "silver": 128,
            "gold": 512,
        },
        "galaxy_brain": {
            "bronze": 1,
            "silver": 10,
            "gold": 25,
        },
        "pair_extraordinaire": {
            "bronze": 1,
            "silver": 10,
            "gold": 24,
        },
    }

    def __init__(self, username: str, token: Optional[str] = None):
        """Initialize tracker for a GitHub user"""
        self.username = username
        self.token = token
        self.headers: Dict[str, str] = {}
        if token:
            self.headers["Authorization"] = f"token {token}"

    def get_user_data(self) -> Dict:
        """Fetch user profile data"""

        url = f"{self.BASE_URL}/users/{self.username}"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code != 200:
            raise Exception(f"User not found: {self.username}")
        return resp.json()

    def count_merged_prs(self) -> int:
        """Count total merged PRs (Pull Shark)"""

        query = f"is:pr is:merged author:{self.username}"
        url = f"{self.BASE_URL}/search/issues"
        params = {"q": query, "per_page": 1}
        resp = requests.get(url, params=params, headers=self.headers)
        data = resp.json()
        return data.get("total_count", 0)

    def count_stars(self) -> Dict[str, int]:
        """Count stars on each repo (Starstruck)"""

        url = f"{self.BASE_URL}/users/{self.username}/repos"
        params = {"type": "owner", "per_page": 100, "sort": "stars"}

        repos = []
        page = 1
        while True:
            params["page"] = page
            resp = requests.get(url, params=params, headers=self.headers)
            if resp.status_code != 200:
                break

            data = resp.json()
            if not data:
                break

            repos.extend(data)
            page += 1

        result = {}
        for repo in repos:
            result[repo["name"]] = repo["stargazers_count"]

        return result

    def get_max_stars(self) -> Tuple[Optional[str], int]:
        """Get repo with most stars"""
        stars = self.count_stars()
        if not stars:
            return None, 0

        max_repo = max(stars.items(), key=lambda x: x[1])
        return max_repo

    def count_discussions_answers(self) -> int:
        """Count accepted discussion answers (Galaxy Brain)

        Note: Requires authenticated request for accurate data
        """
        # GitHub API doesn't expose discussion answers easily
        # This would require GraphQL query
        return 0  # TODO: Implement GraphQL

    def count_coauthored_commits(self) -> int:
        """Count co-authored commits (Pair Extraordinaire)"""

        url = f"{self.BASE_URL}/users/{self.username}/repos"
        params = {"type": "owner", "per_page": 100}

        coauthored = 0
        page = 1

        while True:
            params["page"] = page
            resp = requests.get(url, params=params, headers=self.headers)
            if resp.status_code != 200:
                break

            repos = resp.json()
            if not repos:
                break

            for repo in repos:
                # This is approximate - would need to check each commit
                # For now, skip detailed count
                pass

            page += 1

        return coauthored

    def get_badge_status(self) -> Dict:
        """Get status of all badges"""
        merged_prs = self.count_merged_prs()
        max_repo_result = self.get_max_stars()
        max_repo = max_repo_result[0] if max_repo_result else None
        max_stars = max_repo_result[1] if max_repo_result else 0

        status = {
            "user": self.username,
            "checked_at": datetime.now().isoformat(),
            "badges": {},
        }

        # Pull Shark
        status["badges"]["pull_shark"] = {
            "current": merged_prs,
            "bronze": merged_prs >= self.BADGES["pull_shark"]["bronze"],
            "silver": merged_prs >= self.BADGES["pull_shark"]["silver"],
            "gold": merged_prs >= self.BADGES["pull_shark"]["gold"],
            "progress": f"{merged_prs}/{self.BADGES['pull_shark']['gold']}",
        }

        # Starstruck
        status["badges"]["starstruck"] = {
            "current": max_stars,
            "top_repo": max_repo,
            "bronze": max_stars >= self.BADGES["starstruck"]["bronze"],
            "silver": max_stars >= self.BADGES["starstruck"]["silver"],
            "gold": max_stars >= self.BADGES["starstruck"]["gold"],
            "progress": f"{max_stars}/{self.BADGES['starstruck']['gold']}",
        }

        return status

    def print_status(self):
        """Print formatted badge status"""
        status = self.get_badge_status()

        print("\n" + "=" * 60)
        print(f"🏆 GitHub Badges Status: @{status['user']}")
        print("=" * 60)

        # Pull Shark
        ps = status["badges"]["pull_shark"]
        print(
            f"\n🦈 PULL SHARK: {ps['current']}/{self.BADGES['pull_shark']['gold']} merged PRs"
        )
        print(f"   Bronze (4):  {'✅' if ps['bronze'] else '⏳'} {ps['current']}/4")
        print(f"   Silver (16): {'✅' if ps['silver'] else '⏳'} {ps['current']}/16")
        print(f"   Gold (128):  {'✅' if ps['gold'] else '⏳'} {ps['current']}/128")

        # Starstruck
        ss = status["badges"]["starstruck"]
        print(f"\n🌟 STARSTRUCK: {ss['current']} stars on {ss['top_repo']}")
        print(f"   Bronze (16):   {'✅' if ss['bronze'] else '⏳'} {ss['current']}/16")
        print(f"   Silver (128):  {'✅' if ss['silver'] else '⏳'} {ss['current']}/128")
        print(f"   Gold (512):    {'✅' if ss['gold'] else '⏳'} {ss['current']}/512")

        print("\n" + "=" * 60)
        print(f"Last updated: {status['checked_at']}")
        print("=" * 60 + "\n")

    def get_recommendations(self) -> List[str]:
        """Get recommendations for next badges to target"""
        status = self.get_badge_status()
        recs = []

        ps = status["badges"]["pull_shark"]
        ss = status["badges"]["starstruck"]

        # Pull Shark recommendations
        if not ps["bronze"]:
            remaining = self.BADGES["pull_shark"]["bronze"] - ps["current"]
            recs.append(f"Pull Shark Bronze: {remaining} more merged PRs needed")
        elif not ps["silver"]:
            remaining = self.BADGES["pull_shark"]["silver"] - ps["current"]
            recs.append(f"Pull Shark Silver: {remaining} more merged PRs needed")
        elif not ps["gold"]:
            remaining = self.BADGES["pull_shark"]["gold"] - ps["current"]
            recs.append(f"Pull Shark Gold: {remaining} more merged PRs needed")
        else:
            recs.append("🎉 Pull Shark Gold unlocked!")

        # Starstruck recommendations
        if not ss["bronze"]:
            remaining = self.BADGES["starstruck"]["bronze"] - ss["current"]
            recs.append(
                f"Starstruck Bronze: {remaining} more stars needed on {ss['top_repo']}"
            )
        elif not ss["silver"]:
            remaining = self.BADGES["starstruck"]["silver"] - ss["current"]
            recs.append(f"Starstruck Silver: {remaining} more stars needed")
        elif not ss["gold"]:
            remaining = self.BADGES["starstruck"]["gold"] - ss["current"]
            recs.append(f"Starstruck Gold: {remaining} more stars needed")
        else:
            recs.append("🎉 Starstruck Gold unlocked!")

        return recs


def main():
    """CLI interface"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 badge-tracker.py <username> [--token TOKEN]")
        print("\nExamples:")
        print("  python3 badge-tracker.py Aashish-po")
        print("  python3 badge-tracker.py torvalds --token YOUR_GITHUB_TOKEN")
        sys.exit(1)

    username = sys.argv[1]
    token = None

    if "--token" in sys.argv:
        idx = sys.argv.index("--token")
        if idx + 1 < len(sys.argv):
            token = sys.argv[idx + 1]

    try:
        tracker = GitHubBadgeTracker(username, token)
        tracker.print_status()

        print("📋 Recommendations:")
        for rec in tracker.get_recommendations():
            print(f"  • {rec}")

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
