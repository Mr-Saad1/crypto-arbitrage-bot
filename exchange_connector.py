"""
Exchange Connector Module for Crypto Arbitrage Bot
Handles connections to multiple cryptocurrency exchanges using CCXT
"""
import ccxt
from logger import logger
from config import Config


class ExchangeConnector:
    """Manages connections to multiple crypto exchanges"""
    
    SUPPORTED_EXCHANGES = ['binance', 'coinbase', 'kraken', 'bitget']
    
    def __init__(self):
        """Initialize exchange connectors"""
        self.exchanges = {}
        self._initialize_exchanges()
    
    def _initialize_exchanges(self):
        """Initialize all configured exchanges"""
        try:
            # Binance
            if Config.BINANCE_API_KEY and Config.BINANCE_API_SECRET:
                self.exchanges['binance'] = ccxt.binance({
                    'apiKey': Config.BINANCE_API_KEY,
                    'secret': Config.BINANCE_API_SECRET,
                    'enableRateLimit': True,
                })
                logger.info("✓ Binance exchange connected")
            
            # Coinbase
            if Config.COINBASE_API_KEY and Config.COINBASE_API_SECRET:
                self.exchanges['coinbase'] = ccxt.coinbase({
                    'apiKey': Config.COINBASE_API_KEY,
                    'secret': Config.COINBASE_API_SECRET,
                    'password': Config.COINBASE_PASSPHRASE,
                    'enableRateLimit': True,
                })
                logger.info("✓ Coinbase exchange connected")
            
            # Kraken
            if Config.KRAKEN_API_KEY and Config.KRAKEN_API_SECRET:
                self.exchanges['kraken'] = ccxt.kraken({
                    'apiKey': Config.KRAKEN_API_KEY,
                    'secret': Config.KRAKEN_API_SECRET,
                    'enableRateLimit': True,
                })
                logger.info("✓ Kraken exchange connected")
            
            # Bitget
            if Config.BITGET_API_KEY and Config.BITGET_API_SECRET:
                self.exchanges['bitget'] = ccxt.bitget({
                    'apiKey': Config.BITGET_API_KEY,
                    'secret': Config.BITGET_API_SECRET,
                    'password': Config.BITGET_PASSPHRASE,
                    'enableRateLimit': True,
                })
                logger.info("✓ Bitget exchange connected")
        
        except Exception as e:
            logger.error(f"Error initializing exchanges: {str(e)}")
            raise
    
    def get_price(self, exchange_name, symbol):
        """
        Get current price for a symbol from an exchange
        
        Args:
            exchange_name (str): Name of the exchange
            symbol (str): Trading pair symbol (e.g., BTC/USDT)
        
        Returns:
            dict: Price data with keys: bid, ask, last, timestamp
                  Returns None if error occurs
        """
        try:
            if exchange_name not in self.exchanges:
                logger.warning(f"Exchange {exchange_name} not configured")
                return None
            
            exchange = self.exchanges[exchange_name]
            ticker = exchange.fetch_ticker(symbol)
            
            return {
                'bid': ticker.get('bid'),
                'ask': ticker.get('ask'),
                'last': ticker.get('last'),
                'timestamp': ticker.get('timestamp'),
                'exchange': exchange_name
            }
        
        except ccxt.ExchangeNotAvailable as e:
            logger.warning(f"{exchange_name} not available: {str(e)}")
            return None
        except ccxt.NetworkError as e:
            logger.warning(f"Network error on {exchange_name}: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Error fetching price from {exchange_name}: {str(e)}")
            return None
    
    def get_prices_all_exchanges(self, symbol):
        """
        Get price from all available exchanges
        
        Args:
            symbol (str): Trading pair symbol (e.g., BTC/USDT)
        
        Returns:
            dict: Prices from all exchanges
        """
        prices = {}
        for exchange_name in self.exchanges:
            price_data = self.get_price(exchange_name, symbol)
            if price_data:
                prices[exchange_name] = price_data
        
        return prices
    
    def find_arbitrage_opportunities(self, symbol):
        """
        Find arbitrage opportunities by comparing prices across exchanges
        
        Args:
            symbol (str): Trading pair symbol (e.g., BTC/USDT)
        
        Returns:
            list: List of opportunities with best spread
        """
        prices = self.get_prices_all_exchanges(symbol)
        opportunities = []
        
        if len(prices) < 2:
            return opportunities
        
        # Compare all exchange pairs
        exchange_names = list(prices.keys())
        for i in range(len(exchange_names)):
            for j in range(i + 1, len(exchange_names)):
                buy_exchange = exchange_names[i]
                sell_exchange = exchange_names[j]
                
                buy_price = prices[buy_exchange]['ask']
                sell_price = prices[sell_exchange]['bid']
                
                if buy_price and sell_price:
                    profit_percentage = ((sell_price - buy_price) / buy_price) * 100
                    
                    # Check both directions
                    if profit_percentage > Config.MIN_PROFIT_PERCENTAGE:
                        opportunities.append({
                            'buy_exchange': buy_exchange,
                            'sell_exchange': sell_exchange,
                            'buy_price': buy_price,
                            'sell_price': sell_price,
                            'profit_percentage': profit_percentage,
                            'symbol': symbol
                        })
                    
                    # Check reverse direction
                    buy_price_reverse = prices[sell_exchange]['ask']
                    sell_price_reverse = prices[buy_exchange]['bid']
                    profit_percentage_reverse = ((sell_price_reverse - buy_price_reverse) / buy_price_reverse) * 100
                    
                    if profit_percentage_reverse > Config.MIN_PROFIT_PERCENTAGE:
                        opportunities.append({
                            'buy_exchange': sell_exchange,
                            'sell_exchange': buy_exchange,
                            'buy_price': buy_price_reverse,
                            'sell_price': sell_price_reverse,
                            'profit_percentage': profit_percentage_reverse,
                            'symbol': symbol
                        })
        
        return opportunities
    
    def get_balance(self, exchange_name):
        """
        Get account balance from an exchange
        
        Args:
            exchange_name (str): Name of the exchange
        
        Returns:
            dict: Account balance data or None if error
        """
        try:
            if exchange_name not in self.exchanges:
                return None
            
            exchange = self.exchanges[exchange_name]
            balance = exchange.fetch_balance()
            return balance
        
        except Exception as e:
            logger.error(f"Error fetching balance from {exchange_name}: {str(e)}")
            return None
    
    def is_exchange_available(self, exchange_name):
        """
        Check if an exchange is available and connected
        
        Args:
            exchange_name (str): Name of the exchange
        
        Returns:
            bool: True if exchange is available
        """
        return exchange_name in self.exchanges
    
    def get_available_exchanges(self):
        """
        Get list of available and connected exchanges
        
        Returns:
            list: List of available exchange names
        """
        return list(self.exchanges.keys())
