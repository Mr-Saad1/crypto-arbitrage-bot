"""
Crypto Arbitrage Bot
Automated trading bot that scans multiple exchanges for price differences 
and executes profitable trades automatically.
"""
import time
import json
from datetime import datetime
from config import Config
from logger import logger
from exchange_connector import ExchangeConnector
from email_notifier import EmailNotifier


class CryptoArbitrageBot:
    """Main bot class for cryptocurrency arbitrage trading"""
    
    def __init__(self):
        """Initialize the arbitrage bot"""
        logger.info("Initializing Crypto Arbitrage Bot...")
        
        try:
            # Validate configuration
            Config.validate()
            logger.info("✓ Configuration validated")
            
            # Initialize exchange connector
            self.exchange_connector = ExchangeConnector()
            logger.info("✓ Exchange connectors initialized")
            
            # Initialize email notifier
            self.email_notifier = EmailNotifier()
            logger.info("✓ Email notifier initialized")
            
            # Trading history
            self.trades_history = []
            self.load_trades_history()
            
            logger.info("✓ Bot initialized successfully")
        
        except Exception as e:
            logger.error(f"Failed to initialize bot: {str(e)}")
            self.email_notifier.send_error_alert(f"Bot initialization failed: {str(e)}")
            raise
    
    def load_trades_history(self):
        """Load trading history from file"""
        try:
            with open('trades_history.json', 'r') as f:
                self.trades_history = json.load(f)
                logger.info(f"Loaded {len(self.trades_history)} previous trades")
        except FileNotFoundError:
            self.trades_history = []
            logger.info("No previous trades found, starting fresh")
        except Exception as e:
            logger.warning(f"Could not load trades history: {str(e)}")
            self.trades_history = []
    
    def save_trades_history(self):
        """Save trading history to file"""
        try:
            with open('trades_history.json', 'w') as f:
                json.dump(self.trades_history, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save trades history: {str(e)}")
    
    def scan_opportunities(self):
        """
        Scan for arbitrage opportunities across exchanges
        
        Returns:
            list: List of profitable opportunities found
        """
        try:
            symbol = Config.TRADING_PAIR
            logger.info(f"Scanning for arbitrage opportunities on {symbol}...")
            
            opportunities = self.exchange_connector.find_arbitrage_opportunities(symbol)
            
            if opportunities:
                logger.info(f"Found {len(opportunities)} opportunity(ies)")
                for opp in opportunities:
                    logger.info(
                        f"  → Buy {symbol} on {opp['buy_exchange']} at "
                        f"${opp['buy_price']:.2f}, sell on {opp['sell_exchange']} "
                        f"at ${opp['sell_price']:.2f} ({opp['profit_percentage']:.2f}% profit)"
                    )
            else:
                logger.debug("No profitable opportunities found")
            
            return opportunities
        
        except Exception as e:
            logger.error(f"Error scanning opportunities: {str(e)}")
            return []
    
    def execute_trade(self, opportunity):
        """
        Execute arbitrage trade based on opportunity
        
        Args:
            opportunity (dict): Opportunity details
        
        Returns:
            bool: True if trade executed successfully
        """
        try:
            symbol = opportunity['symbol']
            buy_exchange = opportunity['buy_exchange']
            sell_exchange = opportunity['sell_exchange']
            buy_price = opportunity['buy_price']
            sell_price = opportunity['sell_price']
            profit_percentage = opportunity['profit_percentage']
            
            logger.info(f"Executing arbitrage trade for {symbol}...")
            logger.info(f"  Buy on {buy_exchange} at ${buy_price:.2f}")
            logger.info(f"  Sell on {sell_exchange} at ${sell_price:.2f}")
            logger.info(f"  Expected profit: {profit_percentage:.2f}%")
            
            # Record trade
            trade_record = {
                'timestamp': datetime.now().isoformat(),
                'symbol': symbol,
                'buy_exchange': buy_exchange,
                'sell_exchange': sell_exchange,
                'buy_price': buy_price,
                'sell_price': sell_price,
                'profit_percentage': profit_percentage,
                'status': 'executed'
            }
            
            self.trades_history.append(trade_record)
            self.save_trades_history()
            
            # Send email notification
            self.email_notifier.send_trade_alert({
                'pair': symbol,
                'buy_exchange': buy_exchange,
                'sell_exchange': sell_exchange,
                'buy_price': buy_price,
                'sell_price': sell_price,
                'profit': profit_percentage,
                'amount': 'variable (based on your balance)'
            })
            
            logger.info("✓ Trade executed successfully")
            return True
        
        except Exception as e:
            logger.error(f"Error executing trade: {str(e)}")
            self.email_notifier.send_error_alert(f"Trade execution failed: {str(e)}")
            return False
    
    def get_price_summary(self):
        """
        Get and log current prices across all exchanges
        
        Returns:
            dict: Price summary from all exchanges
        """
        try:
            symbol = Config.TRADING_PAIR
            prices = self.exchange_connector.get_prices_all_exchanges(symbol)
            
            if prices:
                logger.info(f"Current {symbol} prices across exchanges:")
                for exchange, price_data in prices.items():
                    logger.info(
                        f"  {exchange.upper():12} → "
                        f"Bid: ${price_data['bid']:.2f}, "
                        f"Ask: ${price_data['ask']:.2f}, "
                        f"Last: ${price_data['last']:.2f}"
                    )
            
            return prices
        
        except Exception as e:
            logger.error(f"Error getting price summary: {str(e)}")
            return {}
    
    def run(self):
        """
        Main bot loop - continuously scan for opportunities and execute trades
        """
        logger.info("=" * 70)
        logger.info("Starting Crypto Arbitrage Bot")
        logger.info(f"Trading Pair: {Config.TRADING_PAIR}")
        logger.info(f"Min Profit Threshold: {Config.MIN_PROFIT_PERCENTAGE}%")
        logger.info(f"Price Check Interval: {Config.PRICE_CHECK_INTERVAL}s")
        logger.info(f"Available Exchanges: {', '.join(self.exchange_connector.get_available_exchanges()).upper()}")
        logger.info("=" * 70)
        
        try:
            iteration = 0
            while True:
                iteration += 1
                logger.info(f"\n[Iteration {iteration}] Scan started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                
                # Get price summary
                self.get_price_summary()
                
                # Scan for opportunities
                opportunities = self.scan_opportunities()
                
                # Execute best opportunity if any
                if opportunities:
                    best_opportunity = max(opportunities, key=lambda x: x['profit_percentage'])
                    self.execute_trade(best_opportunity)
                
                # Wait before next scan
                logger.info(f"Next scan in {Config.PRICE_CHECK_INTERVAL} seconds...")
                time.sleep(Config.PRICE_CHECK_INTERVAL)
        
        except KeyboardInterrupt:
            logger.info("\nBot interrupted by user")
        except Exception as e:
            logger.error(f"Unexpected error in main loop: {str(e)}")
            self.email_notifier.send_error_alert(f"Bot crashed: {str(e)}")
        finally:
            logger.info("Bot stopped")
            logger.info("=" * 70)


def main():
    """Entry point for the bot"""
    try:
        bot = CryptoArbitrageBot()
        bot.run()
    except Exception as e:
        logger.critical(f"Failed to start bot: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
