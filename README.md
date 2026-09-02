````markdown
# Crypto Arbitrage Bot

A professional-grade automated trading bot that scans multiple cryptocurrency exchanges for price differences and executes profitable trades automatically.

## 🚀 Features

✅ **Real-time Price Monitoring** - Continuously scans Binance, Coinbase, Kraken, and Bitget
✅ **Automatic Trade Execution** - Executes trades when profitable opportunities are detected
✅ **Email Notifications** - Get instant alerts when trades are executed
✅ **24/7 Trading** - Run on a server or locally
✅ **Easy Configuration** - Simple `.env` file setup
✅ **Secure API Handling** - Environment variable-based secrets management
✅ **Comprehensive Logging** - Detailed logs for monitoring and debugging
✅ **Docker Support** - Easy containerized deployment
✅ **Unit Tests** - Built-in test suite for reliability

## 📋 Requirements

- Python 3.9+ (or Docker)
- API keys from supported exchanges:
  - [Binance](https://www.binance.com/en/account/api-management)
  - [Coinbase](https://coinbase.com/settings/api)
  - [Kraken](https://www.kraken.com/settings/api)
  - [Bitget](https://www.bitget.com/settings/api)
- Gmail account with **App Passwords** enabled for email alerts

## 🔧 Installation

### Option 1: Local Installation

```bash
# Clone the repository
git clone https://github.com/Mr-Saad1/crypto-arbitrage-bot.git
cd crypto-arbitrage-bot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure your API keys
cp .env.example .env
nano .env  # Edit with your credentials
```

### Option 2: Docker Installation

```bash
# Build and run with Docker Compose
cp .env.example .env
nano .env  # Edit with your credentials
docker-compose up -d

# View logs
docker-compose logs -f crypto-arbitrage-bot

# Stop the bot
docker-compose down
```

## ⚙️ Configuration

### 1. API Keys Setup

Edit your `.env` file with your exchange credentials:

```env
# Binance
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret

# Coinbase
COINBASE_API_KEY=your_key
COINBASE_API_SECRET=your_secret
COINBASE_PASSPHRASE=your_passphrase

# Kraken
KRAKEN_API_KEY=your_key
KRAKEN_API_SECRET=your_secret

# Bitget
BITGET_API_KEY=your_key
BITGET_API_SECRET=your_secret
BITGET_PASSPHRASE=your_passphrase
```

### 2. Email Notifications Setup

For Gmail:
1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Enable **2-Step Verification** if not already enabled
3. Generate an **App Password** for "Mail" and "Windows Computer"
4. Use this password in your `.env`:

```env
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=your_email@gmail.com
```

### 3. Bot Configuration

```env
# Minimum profit threshold to execute trades
MIN_PROFIT_PERCENTAGE=0.5

# How often to check prices (in seconds)
PRICE_CHECK_INTERVAL=30

# Trading pair to monitor
TRADING_PAIR=BTC/USDT
```

## 🏃 Running the Bot

### Local Execution

```bash
python crypto_bot.py
```

### Docker Execution

```bash
docker-compose up -d
docker-compose logs -f
```

### Background Execution (Linux/Mac)

```bash
nohup python crypto_bot.py > bot.log 2>&1 &
```

### Stop the Bot

```bash
# Local: Press CTRL+C

# Background: pkill -f crypto_bot.py

# Docker: docker-compose down
```

## 📊 Project Structure

```
crypto-arbitrage-bot/
├── crypto_bot.py              # Main bot logic
├── config.py                  # Configuration management
├── exchange_connector.py       # Exchange API integration
├── email_notifier.py          # Email alert system
├── logger.py                  # Logging configuration
├── test_bot.py                # Unit tests
├── requirements.txt           # Python dependencies
├── .env.example              # Configuration template
├── .env                       # Your actual credentials (git ignored)
├── .gitignore                # Git ignore rules
├── Dockerfile                # Docker containerization
├── docker-compose.yml        # Docker Compose setup
├── README.md                 # This file
└── logs/                      # Log files (auto-created)
    └── bot.log               # Application logs
```

## 🧪 Testing

```bash
# Run all tests
python -m pytest test_bot.py -v

# Run with coverage
python -m pytest test_bot.py --cov=. --cov-report=html

# Run specific test
python -m pytest test_bot.py::TestConfig -v
```

## 🚀 Deployment

### Option 1: Local Server

Simply run:
```bash
python crypto_bot.py
```

### Option 2: Linux Server (with systemd)

Create `/etc/systemd/system/crypto-arbitrage-bot.service`:

```ini
[Unit]
Description=Crypto Arbitrage Bot
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/crypto-arbitrage-bot
Environment="PATH=/home/ubuntu/crypto-arbitrage-bot/venv/bin"
ExecStart=/home/ubuntu/crypto-arbitrage-bot/venv/bin/python crypto_bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl daemon-reload
sudo systemctl enable crypto-arbitrage-bot
sudo systemctl start crypto-arbitrage-bot
sudo systemctl status crypto-arbitrage-bot
```

### Option 3: VPS (AWS, DigitalOcean, Linode)

```bash
# SSH into your VPS
ssh ubuntu@your-vps-ip

# Install Python and dependencies
sudo apt-get update
sudo apt-get install python3.11 python3.11-venv python3-pip

# Clone and setup
git clone https://github.com/Mr-Saad1/crypto-arbitrage-bot.git
cd crypto-arbitrage-bot
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create .env with your credentials
nano .env

# Run with nohup or use systemd (see above)
nohup python crypto_bot.py &
```

### Option 4: Docker Deployment

```bash
docker-compose up -d
```

## 📝 Logging

The bot creates detailed logs in `logs/bot.log`:

```
2026-09-02 10:12:50 - crypto_arbitrage_bot - INFO - Initializing Crypto Arbitrage Bot...
2026-09-02 10:12:51 - crypto_arbitrage_bot - INFO - ✓ Exchange connectors initialized
2026-09-02 10:12:52 - crypto_arbitrage_bot - INFO - [Iteration 1] Scan started at 2026-09-02 10:12:52
```

## 🔒 Security Best Practices

⚠️ **IMPORTANT:**

- ✅ **Use `.env` files** - Never commit credentials to git
- ✅ **Keep `.gitignore` updated** - Protects sensitive files
- ✅ **Use API key restrictions** - Enable IP whitelisting on exchanges
- ✅ **Limit API permissions** - Only enable required permissions (e.g., trading only)
- ✅ **Use App Passwords** - Gmail app passwords instead of main password
- ✅ **Monitor logs regularly** - Check for unusual activity
- ✅ **Start with small trades** - Test with minimal amounts first
- ⚠️ **Paper trading first** - Use sandbox/testnet before real funds

## ⚠️ Disclaimer

**This bot executes REAL trades with REAL funds.** 

- Test extensively on a sandbox before using real money
- Start with small amounts to verify functionality
- The developer is NOT responsible for any financial losses
- Crypto trading involves significant financial risk
- Use responsibly and at your own risk

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'ccxt'"
```bash
pip install -r requirements.txt
```

### "Invalid API key" errors
- Verify API keys are correct in `.env`
- Check API key permissions on exchange
- Ensure API key is activated/enabled

### "Email send failed"
- Verify Gmail app password (not main password)
- Enable 2-Step Verification on Gmail
- Check firewall/antivirus isn't blocking SMTP

### "No profitable opportunities found"
- Adjust `MIN_PROFIT_PERCENTAGE` to a lower value
- Check exchange connectivity
- Verify `TRADING_PAIR` is correct

## 📞 Support

- Open an [issue](https://github.com/Mr-Saad1/crypto-arbitrage-bot/issues) on GitHub
- Check existing issues for solutions
- Include logs and configuration details (without API keys!)

## 📄 License

This project is provided as-is for educational and commercial use.

## 📈 Roadmap

- [ ] WebSocket support for real-time prices
- [ ] Database storage for trade history
- [ ] Web dashboard for monitoring
- [ ] Mobile app notifications
- [ ] Advanced profit optimization algorithms
- [ ] Multi-pair trading support
- [ ] Machine learning for prediction

---

**Happy Trading! 🚀**
````
