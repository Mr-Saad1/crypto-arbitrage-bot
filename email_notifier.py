"""
Email notification module for Crypto Arbitrage Bot
Handles sending email alerts for trade execution
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config
from logger import logger


class EmailNotifier:
    """Handles email notifications for trades"""
    
    def __init__(self):
        """Initialize email notifier with config"""
        self.sender_email = Config.EMAIL_SENDER
        self.sender_password = Config.EMAIL_PASSWORD
        self.receiver_email = Config.EMAIL_RECEIVER
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
    
    def send_trade_alert(self, trade_info):
        """
        Send email alert for successful trade execution
        
        Args:
            trade_info (dict): Dictionary containing trade details
                - exchange: Exchange name
                - pair: Trading pair (e.g., BTC/USDT)
                - action: buy/sell
                - buy_price: Price on buying exchange
                - sell_price: Price on selling exchange
                - profit: Profit percentage
                - amount: Trade amount
        
        Returns:
            bool: True if email sent successfully, False otherwise
        """
        try:
            subject = f"🚀 Arbitrage Trade Executed - {trade_info.get('pair', 'N/A')}"
            
            body = self._format_email_body(trade_info)
            
            self._send_email(subject, body)
            logger.info(f"Trade alert email sent to {self.receiver_email}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send email notification: {str(e)}")
            return False
    
    def send_error_alert(self, error_message):
        """
        Send email alert for bot errors
        
        Args:
            error_message (str): Error message to send
        
        Returns:
            bool: True if email sent successfully, False otherwise
        """
        try:
            subject = "⚠️ Crypto Arbitrage Bot - Error Alert"
            body = f"An error occurred in the bot:\n\n{error_message}"
            
            self._send_email(subject, body)
            logger.info(f"Error alert email sent to {self.receiver_email}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send error email: {str(e)}")
            return False
    
    def _format_email_body(self, trade_info):
        """Format trade information into email body"""
        body = f"""
Arbitrage Opportunity Executed!

Exchange Pair: {trade_info.get('pair', 'N/A')}
Buy Exchange: {trade_info.get('buy_exchange', 'N/A')}
Sell Exchange: {trade_info.get('sell_exchange', 'N/A')}

Buy Price: ${trade_info.get('buy_price', 'N/A')}
Sell Price: ${trade_info.get('sell_price', 'N/A')}

Trade Amount: {trade_info.get('amount', 'N/A')} {trade_info.get('pair', '').split('/')[0]}
Profit: {trade_info.get('profit', 'N/A')}%

Status: ✅ Successfully Executed

---
Crypto Arbitrage Bot
        """
        return body
    
    def _send_email(self, subject, body):
        """
        Send email using SMTP
        
        Args:
            subject (str): Email subject
            body (str): Email body content
        
        Raises:
            Exception: If email fails to send
        """
        # Create message
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = self.sender_email
        message["To"] = self.receiver_email
        
        # Attach body
        message.attach(MIMEText(body, "plain"))
        
        # Send email
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, self.receiver_email, message.as_string())


def send_notification(subject, body):
    """
    Utility function to send email notification
    
    Args:
        subject (str): Email subject
        body (str): Email body
    
    Returns:
        bool: Success status
    """
    try:
        notifier = EmailNotifier()
        notifier._send_email(subject, body)
        return True
    except Exception as e:
        logger.error(f"Failed to send notification: {str(e)}")
        return False
