# Quick Start Guide

## ⚡ 5-Minute Setup

### Step 1: Clone and Install (2 minutes)

```bash
git clone https://github.com/Mr-Saad1/crypto-arbitrage-bot.git
cd crypto-arbitrage-bot
make setup
```

### Step 2: Configure (2 minutes)

```bash
# Edit .env file with your credentials
nano .env

# Required:
# - BINANCE_API_KEY and BINANCE_API_SECRET
# - EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER
```

### Step 3: Run (1 minute)

```bash
# Run the bot
make run

# Or with Docker
make docker-run
```

## 📋 Prerequisites

### API Keys

1. **Binance** (required): https://www.binance.com/en/account/api-management
   - ✅ Enable Spot Trading
   - ✅ Restrict to your IP

2. **Coinbase** (optional): https://coinbase.com/settings/api
3. **Kraken** (optional): https://www.kraken.com/settings/api
4. **Bitget** (optional): https://www.bitget.com/settings/api

### Email Setup (for notifications)

1. Google Account → Security
2. Enable 2-Step Verification
3. Generate App Password for "Mail"
4. Use that password in .env

## 🏃 Common Commands

```bash
make test          # Run tests
make lint          # Check code quality
make run           # Run the bot
make docker-run    # Run in Docker
make docker-stop   # Stop Docker
make clean         # Clean up
make help          # Show all commands
```

## 🔍 Verify Installation

```bash
# Check Python version
python --version  # Should be 3.9+

# Run tests
make test  # All tests should pass ✓

# Check configuration
python -c "from config import Config; Config.validate()"
# Should print: ✓ Configuration validated successfully!
```

## 📊 First Run

```bash
# Start the bot
make run

# Expected output:
# 2026-09-02 10:12:50 - crypto_arbitrage_bot - INFO - Initializing...
# 2026-09-02 10:12:51 - crypto_arbitrage_bot - INFO - ✓ Exchange connectors initialized
# 2026-09-02 10:12:52 - crypto_arbitrage_bot - INFO - [Iteration 1] Scan started...

# Stop: Press CTRL+C
```

## ⚠️ Important Notes

1. **Test First**: Start with a small amount or paper trading
2. **Monitor Logs**: Check `logs/bot.log` for errors
3. **Security**: Never commit your .env file
4. **API Limits**: Exchanges have rate limits - adjust PRICE_CHECK_INTERVAL if needed

## 🆘 Troubleshooting

### "No module named 'ccxt'"
```bash
pip install -r requirements.txt
```

### "Invalid API key"
```bash
# Verify in .env file
# Check exchange API settings
# Ensure API key is enabled
```

### "Email send failed"
```bash
# Use App Password (not main password)
# Enable 2-Step Verification
# Check EMAIL_PASSWORD in .env
```

### "No profitable opportunities"
```bash
# Lower MIN_PROFIT_PERCENTAGE in .env
# Check TRADING_PAIR is correct
# Verify exchange connectivity
```

## 📚 Next Steps

1. Read [README.md](README.md) for detailed documentation
2. Configure multiple exchanges for better opportunities
3. Set up deployment on a VPS for 24/7 trading
4. Monitor logs and trades regularly
5. Consider contributing improvements!

## 🚀 Ready?

```bash
make run
```

Happy trading! 🎉
