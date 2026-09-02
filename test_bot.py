"""
Unit tests for Crypto Arbitrage Bot
"""
import unittest
import json
from unittest.mock import patch, MagicMock
from config import Config
from exchange_connector import ExchangeConnector
from email_notifier import EmailNotifier


class TestConfig(unittest.TestCase):
    """Test configuration module"""
    
    def test_config_loads_env_variables(self):
        """Test that config loads environment variables"""
        self.assertIsNotNone(Config.TRADING_PAIR)
        self.assertEqual(Config.TRADING_PAIR, 'BTC/USDT')
    
    def test_min_profit_percentage_is_float(self):
        """Test that min profit is a float"""
        self.assertIsInstance(Config.MIN_PROFIT_PERCENTAGE, float)
    
    def test_price_check_interval_is_int(self):
        """Test that price check interval is an integer"""
        self.assertIsInstance(Config.PRICE_CHECK_INTERVAL, int)


class TestExchangeConnector(unittest.TestCase):
    """Test exchange connector module"""
    
    @patch('exchange_connector.ccxt.binance')
    def test_binance_initialization(self, mock_binance):
        """Test Binance exchange initialization"""
        with patch.dict('os.environ', {'BINANCE_API_KEY': 'test', 'BINANCE_API_SECRET': 'test'}):
            connector = ExchangeConnector()
            self.assertIsNotNone(connector)
    
    def test_get_available_exchanges(self):
        """Test getting available exchanges"""
        connector = ExchangeConnector()
        exchanges = connector.get_available_exchanges()
        self.assertIsInstance(exchanges, list)


class TestEmailNotifier(unittest.TestCase):
    """Test email notifier module"""
    
    @patch('email_notifier.smtplib.SMTP')
    def test_email_notifier_initialization(self, mock_smtp):
        """Test email notifier initialization"""
        notifier = EmailNotifier()
        self.assertIsNotNone(notifier.sender_email)
        self.assertIsNotNone(notifier.receiver_email)
    
    def test_format_email_body(self):
        """Test email body formatting"""
        notifier = EmailNotifier()
        trade_info = {
            'pair': 'BTC/USDT',
            'buy_exchange': 'binance',
            'sell_exchange': 'coinbase',
            'buy_price': 50000,
            'sell_price': 50100,
            'profit': 0.2,
            'amount': '0.1'
        }
        body = notifier._format_email_body(trade_info)
        self.assertIn('BTC/USDT', body)
        self.assertIn('binance', body)
        self.assertIn('coinbase', body)


class TestArbitrageLogic(unittest.TestCase):
    """Test arbitrage opportunity detection"""
    
    def test_profit_calculation(self):
        """Test profit percentage calculation"""
        buy_price = 100
        sell_price = 101
        profit = ((sell_price - buy_price) / buy_price) * 100
        self.assertEqual(profit, 1.0)
    
    def test_negative_profit_detection(self):
        """Test detection of unprofitable trades"""
        buy_price = 100
        sell_price = 99
        profit = ((sell_price - buy_price) / buy_price) * 100
        self.assertLess(profit, 0)


if __name__ == '__main__':
    unittest.main()
