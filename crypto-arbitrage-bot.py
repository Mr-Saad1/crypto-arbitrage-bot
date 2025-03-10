import time
import ccxt
import smtplib
from email.mime.text import MIMEText

def get_price(coin_id, exchange):
    try:
        exchange_api = getattr(ccxt, exchange)()
        ticker = exchange_api.fetch_ticker(f"{coin_id}/USDT")
        return ticker['last']
    except Exception as e:
        print(f"Error fetching data from {exchange}: {e}")
        return None

def send_email(subject, message):
    sender_email = "your_email@gmail.com"
    receiver_email = "your_email@gmail.com"
    password = "your_email_password"
    
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def execute_trade(exchange, order_type, coin_id, amount):
    try:
        exchange_api = getattr(ccxt, exchange)()
        exchange_api.apiKey = "your_api_key"
        exchange_api.secret = "your_api_secret"
        
        if order_type == "buy":
            order = exchange_api.create_market_buy_order(f"{coin_id}/USDT", amount)
        else:
            order = exchange_api.create_market_sell_order(f"{coin_id}/USDT", amount)
        
        print(f"Trade executed: {order_type} {amount} {coin_id} on {exchange}")
        return order
    except Exception as e:
        print(f"Error executing trade on {exchange}: {e}")
        return None

def arbitrage_opportunity():
    exchanges = ['binance', 'coinbase', 'kraken']  # Updated coinbasepro to coinbase
    coins = ['BTC', 'ETH', 'SOL']
    
    for coin_id in coins:
        prices = {}
        for exchange in exchanges:
            price = get_price(coin_id, exchange)
            if price:
                prices[exchange] = price
        
        if len(prices) < 2:
            print(f"Not enough data for {coin_id} arbitrage analysis.")
            continue
        
        min_exchange = min(prices, key=prices.get)
        max_exchange = max(prices, key=prices.get)
        
        min_price = prices[min_exchange]
        max_price = prices[max_exchange]
        
        profit = max_price - min_price
        percentage_profit = (profit / min_price) * 100
        
        print(f"\n{coin_id}:")
        print(f"Lowest Price: {min_price} on {min_exchange}")
        print(f"Highest Price: {max_price} on {max_exchange}")
        print(f"Potential Arbitrage Profit: ${profit:.2f} ({percentage_profit:.2f}%)")
        
        if percentage_profit > 0.5:  # Reduced threshold from 1% to 0.5%
            print("Arbitrage opportunity found! Buying and selling...")
            execute_trade(min_exchange, "buy", coin_id, 0.01)  # Adjust amount as needed
            execute_trade(max_exchange, "sell", coin_id, 0.01)
            
            email_subject = f"Arbitrage Alert: {coin_id}"
            email_message = f"Buy from {min_exchange} at ${min_price}, sell on {max_exchange} at ${max_price}. Profit: ${profit:.2f} ({percentage_profit:.2f}%)"
            send_email(email_subject, email_message)
        else:
            print("No significant arbitrage opportunity at the moment.")

while True:
    arbitrage_opportunity()
    time.sleep(30)