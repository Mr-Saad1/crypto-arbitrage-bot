#!/usr/bin/env python3
"""
Quick Run Script - Execute Crypto Arbitrage Bot Directly from GitHub
Downloads and runs the bot without cloning
"""

import os
import sys
import subprocess
import urllib.request
import zipfile
from pathlib import Path

print("\n" + "="*80)
print("🚀 CRYPTO ARBITRAGE BOT - QUICK START FROM GITHUB")
print("="*80 + "\n")

# Create temp directory
temp_dir = Path("crypto_arbitrage_bot_temp")
bot_dir = Path("crypto_arbitrage_bot")

try:
    # Step 1: Download repo
    print("📥 Downloading bot files from GitHub...")
    repo_url = "https://github.com/Mr-Saad1/crypto-arbitrage-bot/archive/refs/heads/main.zip"
    zip_path = "bot.zip"
    
    urllib.request.urlretrieve(repo_url, zip_path)
    print("   ✓ Downloaded successfully\n")
    
    # Step 2: Extract
    print("📦 Extracting files...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    
    # Find extracted folder
    extracted_folder = None
    for item in temp_dir.iterdir():
        if item.is_dir():
            extracted_folder = item
            break
    
    if extracted_folder:
        # Copy to final location
        if bot_dir.exists():
            import shutil
            shutil.rmtree(bot_dir)
        extracted_folder.rename(bot_dir)
        temp_dir.rmdir()
        print("   ✓ Files extracted\n")
    
    os.remove(zip_path)
    os.chdir(bot_dir)
    
    # Step 3: Install dependencies
    print("📚 Installing dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "python-dotenv"], check=True)
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "ccxt"], check=True)
    print("   ✓ Dependencies installed\n")
    
    # Step 4: Run the bot
    print("="*80)
    print("🤖 STARTING BOT")
    print("="*80 + "\n")
    
    subprocess.run([sys.executable, "run_bot.py"])

except KeyboardInterrupt:
    print("\n\n✓ Bot stopped")
except Exception as e:
    print(f"\n✗ Error: {e}")
    sys.exit(1)
