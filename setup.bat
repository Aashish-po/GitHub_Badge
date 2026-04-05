@echo off
REM Quick setup script for GitHub Badges repo (Windows)

echo.
echo 🚀 GitHub Badges: Hack ^& Genius - Setup
echo ========================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git not found. Please install Git for Windows first.
    echo Download: https://git-scm.com/download/win
    pause
    exit /b 1
)

REM Check if gh CLI is installed
gh --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  GitHub CLI (gh) not found.
    echo Some features require GitHub CLI.
    echo Download: https://cli.github.com/
    echo.
)

REM Create necessary directories
echo 📁 Creating directory structure...
if not exist badges mkdir badges
if not exist badges\pull-shark mkdir badges\pull-shark
if not exist badges\pull-shark\tools mkdir badges\pull-shark\tools
if not exist badges\starstruck mkdir badges\starstruck
if not exist badges\starstruck\tools mkdir badges\starstruck\tools
if not exist badges\galaxy-brain mkdir badges\galaxy-brain
if not exist badges\quickdraw mkdir badges\quickdraw
if not exist badges\pair-extraordinaire mkdir badges\pair-extraordinaire
if not exist badges\yolo mkdir badges\yolo
if not exist badges\sponsor mkdir badges\sponsor
if not exist tools mkdir tools
if not exist guides mkdir guides

echo ✅ Directories created
echo.

REM Initialize git if needed
if not exist .git (
    echo 📝 Initializing git repository...
    git init
    echo ✅ Git initialized
    echo.
)

REM Suggest next steps
echo 📋 Next steps:
echo.
echo 1️⃣  Configure git (if new):
echo     git config user.name "Your Name"
echo     git config user.email "your@email.com"
echo.

echo 2️⃣  Connect to GitHub:
echo     gh auth login
echo.

echo 3️⃣  Install Python dependencies (optional):
echo     pip install requests
echo.

echo 4️⃣  Run badge tracker:
echo     python tools\badge-tracker.py YOUR-USERNAME
echo.

echo 5️⃣  Read the guides:
echo     type QUICK_START.md
echo     type GENIUS_METHODS.md
echo.

echo 6️⃣  Start contributing:
echo     type CONTRIBUTING.md
echo.

echo ✨ Setup complete!
echo.
echo Happy badge hunting! 🏆
echo.
pause
