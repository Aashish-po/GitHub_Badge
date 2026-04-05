#!/bin/bash
# Quick setup script for GitHub Badges repo

set -e

echo "🚀 GitHub Badges: Hack & Genius - Setup"
echo "========================================"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git not found. Please install git first."
    exit 1
fi

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "⚠️  GitHub CLI (gh) not found."
    echo "Some features require GitHub CLI."
    echo "Install: https://cli.github.com/"
    echo ""
fi

# Create necessary directories
echo "📁 Creating directory structure..."
mkdir -p badges/{pull-shark,starstruck,galaxy-brain,quickdraw,pair-extraordinaire,yolo,sponsor}/tools
mkdir -p tools
mkdir -p guides

echo "✅ Directories created"
echo ""

# Initialize git if needed
if [ ! -d .git ]; then
    echo "📝 Initializing git repository..."
    git init
    echo "✅ Git initialized"
    echo ""
fi

# Suggest next steps
echo "📋 Next steps:"
echo ""
echo "1️⃣  Configure git (if new):"
echo "    git config user.name 'Your Name'"
echo "    git config user.email 'your@email.com'"
echo ""

echo "2️⃣  Connect to GitHub:"
echo "    gh auth login"
echo ""

echo "3️⃣  Install Python dependencies (optional):"
echo "    pip install requests"
echo ""

echo "4️⃣  Run badge tracker:"
echo "    python3 tools/badge-tracker.py YOUR-USERNAME"
echo ""

echo "5️⃣  Read the guides:"
echo "    cat QUICK_START.md"
echo "    cat GENIUS_METHODS.md"
echo ""

echo "6️⃣  Start contributing:"
echo "    cat CONTRIBUTING.md"
echo ""

echo "✨ Setup complete!"
echo ""
echo "Happy badge hunting! 🏆"
