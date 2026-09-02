#!/usr/bin/env python3
"""
Demo mode for Crypto Arbitrage Bot
This runs the bot without requiring real exchange API keys
Perfect for testing and understanding how the bot works
"""
import os
import sys
import time
from datetime import datetime

# Create a mock environment if .env doesn't exist
if not os.path.exists('.env'):
    print("📝 Creating .env file with demo configuration...")
    with open('.env', 'w') as f:
        f.write("""# Demo Configuration
BINANCE_API_KEY=demo_key_12345
BINANCE_API_SECRET=demo_secret_67890

COINBASE_API_KEY=demo_key_coinbase
COINBASE_API_SECRET=demo_secret_coinbase
COINBASE_PASSPHRASE=demo_pass

KRAKEN_API_KEY=demo_key_kraken
KRAKEN_API_SECRET=demo_secret_kraken

BITGET_API_KEY=demo_key_bitget
BITGET_API_SECRET=demo_secret_bitget
BITGET_PASSPHRASE=demo_pass

EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=your_email@gmail.com

MIN_PROFIT_PERCENTAGE=0.5
PRICE_CHECK_INTERVAL=5
TRADING_PAIR=BTC/USDT
LOG_LEVEL=INFO
LOG_FILE=logs/bot.log
""")
    print("✓ .env file created with demo configuration")
    print("  (You can edit it later with your real API keys)\n")

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

print("=" * 70)
print("🚀 Crypto Arbitrage Bot - DEMO MODE")
print("=" * 70)
print()

# Import after .env is created
try:
    from config import Config
    from logger import logger
    
    print("✓ Configuration loaded")
    print(f"  Trading Pair: {Config.TRADING_PAIR}")
    print(f"  Min Profit: {Config.MIN_PROFIT_PERCENTAGE}%")
    print(f"  Check Interval: {Config.PRICE_CHECK_INTERVAL}s")
    print()
    
except Exception as e:
    print(f"✗ Error loading configuration: {e}")
    print("  Make sure all required packages are installed:")
    print("  pip install -r requirements.txt")
    sys.exit(1)

try:
    from exchange_connector import ExchangeConnector
    print("✓ Exchange connector loaded")
except Exception as e:
    print(f"⚠ Exchange connector warning: {e}")
    print("  This is normal if API keys are not configured yet")

try:
    from email_notifier import EmailNotifier
    print("✓ Email notifier loaded")
except Exception as e:
    print(f"⚠ Email notifier warning: {e}")
    print("  This is normal if email is not configured yet")

print()
print("=" * 70)
print("📊 DEMO MODE - Simulated Trading")
print("=" * 70)
print()

# Simulated prices for demo
demo_prices = {
    'iteration': 0,
    'binance': {'ask': 43850, 'bid': 43840, 'last': 43845},
    'coinbase': {'ask': 43920, 'bid': 43910, 'last': 43915},
    'kraken': {'ask': 43880, 'bid': 43870, 'last': 43875},
}

demo_opportunities = [
    {'buy_exchange': 'binance', 'sell_exchange': 'coinbase', 'profit': 0.16},
    {'buy_exchange': 'binance', 'sell_exchange': 'kraken', 'profit': 0.07},
]

def print_price_summary():
    """Print simulated price summary"""
    print(f"  Binance:  Ask ${demo_prices['binance']['ask']}, Bid ${demo_prices['binance']['bid']}")
    print(f"  Coinbase: Ask ${demo_prices['coinbase']['ask']}, Bid ${demo_prices['coinbase']['bid']}")
    print(f"  Kraken:   Ask ${demo_prices['kraken']['ask']}, Bid ${demo_prices['kraken']['bid']}")

def print_opportunities():
    """Print simulated opportunities"""
    for opp in demo_opportunities:
        print(f"  ✓ BUY on {opp['buy_exchange'].upper()} → SELL on {opp['sell_exchange'].upper()}: {opp['profit']:.2f}% profit")

try:
    iteration = 0
    while iteration < 5:  # Run 5 iterations in demo
        iteration += 1
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        print(f"[Iteration {iteration}] Scan at {timestamp}")
        print()
        
        # Print prices
        print("📊 Current Prices (Simulated):")
        print_price_summary()
        print()
        
        # Print opportunities
        if iteration % 2 == 1:  # Find opportunities on odd iterations
            print("🔍 Scanning for opportunities...")
            print_opportunities()
            print()
            print("✅ Trade would be executed!")
            print()
        else:
            print("🔍 No profitable opportunities found")
            print()
        
        # Show info
        print(f"⏰ Next scan in {Config.PRICE_CHECK_INTERVAL}s...")
        print("-" * 70)
        print()
        
        # Wait
        if iteration < 5:
            time.sleep(Config.PRICE_CHECK_INTERVAL)
    
    print()
    print("=" * 70)
    print("✅ DEMO COMPLETE")
    print("=" * 70)
    print()
    print("📝 Next Steps:")
    print("  1. Get API keys from exchanges:")
    print("     • Binance: https://www.binance.com/en/account/api-management")
    print("     • Coinbase: https://coinbase.com/settings/api")
    print("     • Kraken: https://www.kraken.com/settings/api")
    print("     • Bitget: https://www.bitget.com/settings/api")
    print()
    print("  2. Update your .env file with real API keys")
    print()
    print("  3. Run the real bot:")
    print("     python crypto_bot.py")
    print()
    print("  4. Or use Docker:")
    print("     docker-compose up")
    print()
    print("📚 Documentation: https://github.com/Mr-Saad1/crypto-arbitrage-bot")
    print()

except KeyboardInterrupt:
    print()
    print("\n⏹ Demo interrupted by user")
except Exception as e:
    logger.error(f"Error in demo: {e}")
    print(f"\n✗ Error: {e}")
    sys.exit(1)
