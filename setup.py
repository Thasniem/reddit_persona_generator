#!/usr/bin/env python3
"""
Setup script for Reddit Persona Generator
"""

import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def setup_config():
    """Setup configuration files"""
    print("⚙️ Setting up configuration...")
    
    praw_ini = Path("praw.ini")
    praw_example = Path("praw.ini.example")
    
    if not praw_ini.exists() and praw_example.exists():
        print("📋 Creating praw.ini from example...")
        praw_ini.write_text(praw_example.read_text())
        print("⚠️  Please edit praw.ini with your Reddit API credentials!")
        print("   Get credentials from: https://www.reddit.com/prefs/apps")
    elif praw_ini.exists():
        print("✅ praw.ini already exists")
    
    # Create output directory
    Path("outputs").mkdir(exist_ok=True)
    Path("data").mkdir(exist_ok=True)
    print("✅ Created output directories")

def main():
    print("🚀 Setting up Reddit Persona Generator...")
    
    if install_requirements():
        setup_config()
        print("\n🎉 Setup complete!")
        print("\n📝 Next steps:")
        print("1. Edit praw.ini with your Reddit API credentials")
        print("2. Run: python main.py https://reddit.com/user/username")
    else:
        print("\n❌ Setup failed. Please check error messages above.")

if __name__ == "__main__":
    main()
