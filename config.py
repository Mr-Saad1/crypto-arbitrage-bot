"""
Configuration module for Crypto Arbitrage Bot
Loads settings from environment variables
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Main configuration class"""
    
    # Exchange API Keys
    BINANCE_API_KEY = os.getenv('BINANCE_API_KEY', '')
    BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET', '')
    
    COINBASE_API_KEY = os.getenv('COINBASE_API_KEY', '')
    COINBASE_API_SECRET = os.getenv('COINBASE_API_SECRET', '')
    COINBASE_PASSPHRASE = os.getenv('COINBASE_PASSPHRASE', '')
    
    KRAKEN_API_KEY = os.getenv('KRAKEN_API_KEY', '')
    KRAKEN_API_SECRET = os.getenv('KRAKEN_API_SECRET', '')
    
    BITGET_API_KEY = os.getenv('BITGET_API_KEY', '')
    BITGET_API_SECRET = os.getenv('BITGET_API_SECRET', '')
    BITGET_PASSPHRASE = os.getenv('BITGET_PASSPHRASE', '')
    
    # Email Configuration
    EMAIL_SENDER = os.getenv('EMAIL_SENDER', '')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', '')
    EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER', '')
    
    # Bot Configuration
    MIN_PROFIT_PERCENTAGE = float(os.getenv('MIN_PROFIT_PERCENTAGE', '0.5'))
    PRICE_CHECK_INTERVAL = int(os.getenv('PRICE_CHECK_INTERVAL', '30'))
    TRADING_PAIR = os.getenv('TRADING_PAIR', 'BTC/USDT')
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'logs/bot.log')
    
    @staticmethod
    def validate():
        """Validate that all required configurations are present"""
        required_vars = [
            'BINANCE_API_KEY', 'BINANCE_API_SECRET',
            'EMAIL_SENDER', 'EMAIL_PASSWORD', 'EMAIL_RECEIVER'
        ]
        
        missing = []
        for var in required_vars:
            if not getattr(Config, var):
                missing.append(var)
        
        if missing:
            raise ValueError(f"Missing required configuration variables: {', '.join(missing)}")
        
        return True


if __name__ == "__main__":
    Config.validate()
    print("✓ Configuration validated successfully!")
