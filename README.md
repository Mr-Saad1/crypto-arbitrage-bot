# crypto-arbitrage-bot

# Crypto Arbitrage Bot

# Overview
The Crypto Arbitrage Bot is an automated trading bot that scans multiple exchanges (Binance, Coinbase Pro, Kraken, Bitget) for price differences and executes profitable trades automatically. It also sends email alerts whenever an arbitrage opportunity is detected.

# Features
- Real-time price monitoring across multiple exchanges
- Automatic trading execution on profitable opportunities
- Email notifications for trade execution
- Easy customization for different cryptocurrencies
- Can run 24/7 on a server or locally

# Requirements
- Python 3.x installed
- API keys from supported exchanges
- A Gmail account for email alerts (or another SMTP provider)

# Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/crypto-arbitrage-bot.git
   cd crypto-arbitrage-bot
   ```
2. Install required dependencies:
   ```bash
   pip install ccxt smtplib
   ```

# Setup
# 1. Configure API Keys
Open the `crypto_bot.py` file and replace the placeholders with your actual API keys:
```python
exchange_api.apiKey = "your_api_key"
exchange_api.secret = "your_api_secret"
```
If using Bitget, also add your passphrase:
```python
exchange_api.password = "your_api_passphrase"
```

# 2. Configure Email Notifications
Replace email details in `send_email()` function:
```python
sender_email = "your_email@gmail.com"
receiver_email = "your_email@gmail.com"
password = "your_email_password"
```
If using Gmail, enable **App Passwords** in your Google account security settings.

# Running the Bot
To start the bot, simply run:
```bash
python crypto_bot.py
```
This will continuously monitor the exchanges and execute trades automatically when arbitrage opportunities arise.

# Deployment for 24/7 Trading
To run the bot 24/7, you can deploy it on a server:

# Option 1: Deploy on PythonAnywhere
1. Upload the `crypto_bot.py` script to PythonAnywhere.
2. Open a **Bash Console** and install dependencies:
   ```bash
   pip install ccxt smtplib
   ```
3. Run the bot in the background:
   ```bash
   nohup python3 crypto_bot.py &
   ```
4. Add a scheduled task to restart the bot every hour.

# Option 2: Deploy on a VPS (AWS, DigitalOcean, etc.)
1. Set up a VPS and install Python.
2. Clone this repository and install dependencies.
3. Run the bot in the background using `screen`:
   ```bash
   screen -S arbitrage_bot
   python3 crypto_bot.py
   ```
   Press `CTRL+A` then `D` to detach and keep running in the background.

# Monitoring & Stopping the Bot
- The bot will send an **email notification** when a trade is executed.
- To **stop the bot**, use:
  ```bash
  pkill -f crypto_bot.py
  ```
- Adjust `time.sleep(30)` in the script to change the frequency of price checks.

# Disclaimer
This bot executes real trades and involves financial risk. Use it responsibly and test in a sandbox environment before deploying with real funds.

# Contact & Support
If you need help, open an **issue** on GitHub or reach out! 
