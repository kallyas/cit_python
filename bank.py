import sys
import os
from datetime import datetime
from time import sleep
import secrets
import hashlib
import mysql.connector
import re
from typing import Union, Tuple, Optional, List, Dict
import logging
from dotenv import load_dotenv
import getpass

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='bank_system.log'
)
logger = logging.getLogger('BankSystem')

# Load environment variables for database configuration
load_dotenv()

class DatabaseConnection:
    """Database connection manager using context manager pattern"""
    
    def __init__(self):
        """Initialize database connection parameters from environment variables"""
        self.host = os.getenv('DB_HOST', 'localhost')
        self.user = os.getenv('DB_USER', 'root')
        self.password = os.getenv('DB_PASSWORD', '')
        self.database = os.getenv('DB_NAME', 'bank')
        self.connection = None
        self.cursor = None
    
    def __enter__(self):
        """Establish database connection when entering context"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor(buffered=True)
            return self.connection, self.cursor
        except mysql.connector.Error as err:
            logger.error(f"Database connection error: {err}")
            print(f"Database error: {err}")
            sys.exit(1)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close database connection when exiting context"""
        if exc_type is not None:
            logger.error(f"Database operation error: {exc_val}")
            if self.connection:
                self.connection.rollback()
        
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


class Bank:
    """
    Banking system class with improved security and error handling
    
    Attributes:
        name (str): Customer name
        phone (str): Customer phone number
        pin (str): Hashed PIN for account security
        account_number (str): Generated account number
        balance (int): Account balance
        account_number_login (str): Currently logged-in account number
        login_attempts (int): Number of login attempts
        MAX_LOGIN_ATTEMPTS (int): Maximum allowed login attempts
    """
    # Class constants
    MAX_LOGIN_ATTEMPTS = 3
    VALID_PHONE_PREFIXES = ('077', '078', '076', '070', '075')
    
    def __init__(self, name: str = "", phone: str = "", pin: Union[str, int] = ""):
        self.name = name
        self.phone = phone
        # Only hash pin if it's provided (for login scenarios)
        self.pin = self._hash_pin(str(pin)) if pin else ""
        self.account_number = self._generate_account_number() if phone else ""
        self.balance = 0
        self.account_number_login = ''
        self.login_attempts = 0
        
        # Initialize database if not empty constructor
        if name and phone and pin:
            self._setup_database()
    
    def _setup_database(self):
        """Set up database tables if they don't exist"""
        try:
            with DatabaseConnection() as (conn, cursor):
                # Create tables with better constraints and relations
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS bank (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(255) NOT NULL, 
                        phone VARCHAR(15) NOT NULL,
                        pin VARCHAR(255) NOT NULL, 
                        account_number VARCHAR(20) NOT NULL UNIQUE,
                        balance DECIMAL(15,2) NOT NULL DEFAULT 0.00,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                        last_login DATETIME,
                        active BOOLEAN DEFAULT TRUE,
                        INDEX (phone),
                        INDEX (account_number)
                    )
                ''')
                
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS transactions (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        account_number VARCHAR(20) NOT NULL,
                        transaction_type ENUM('deposit', 'withdraw', 'transfer_out', 'transfer_in') NOT NULL,
                        amount DECIMAL(15,2) NOT NULL,
                        recipient_account VARCHAR(20),
                        date DATETIME DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (account_number) REFERENCES bank(account_number) ON DELETE CASCADE,
                        INDEX (account_number),
                        INDEX (date)
                    )
                ''')
                
                conn.commit()
                logger.info("Database tables created or already exist")
        except mysql.connector.Error as err:
            logger.error(f"Database setup error: {err}")
            print(f"Error setting up database: {err}")
            sys.exit(1)

    def _hash_pin(self, pin: str) -> str:
        """Hash PIN with salt for security"""
        # Use a stronger hashing method with salt
        salt = os.getenv('PIN_SALT', 'DEFAULT_SALT_VALUE')
        return hashlib.sha256((pin + salt).encode()).hexdigest()
    
    def _generate_account_number(self) -> str:
        """
        Generate a unique account number format: AC + last 4 digits of phone + timestamp + random digits
        """
        if not self.phone:
            return ""
            
        timestamp = datetime.now().strftime('%Y%m%d%H%M')
        random_part = str(secrets.randbelow(10000)).zfill(4)
        phone_part = self.phone[-4:] if len(self.phone) >= 4 else self.phone
        
        account_number = f"AC{phone_part}{timestamp}{random_part}"
        return account_number[:20]  # Limit to 20 chars max
    
    def create_account(self) -> bool:
        """
        Create a new bank account
        
        Returns:
            bool: True if account created successfully, False otherwise
        """
        # Validate input data
        if not self._validate_account_data():
            return False
            
        # Check if phone number already exists
        if self._phone_exists():
            print("An account with this phone number already exists.")
            return False
            
        try:
            with DatabaseConnection() as (conn, cursor):
                sql = ("INSERT INTO bank (name, phone, pin, account_number, balance)"
                      "VALUES (%s, %s, %s, %s, %s)")
                data = (self.name, self.phone, self.pin, self.account_number, self.balance)
                
                cursor.execute(sql, data)
                conn.commit()
                
                print('\033[92mAccount created successfully!\033[0m')
                print(f'Your account number is: \033[1m{self.account_number}\033[0m')
                logger.info(f"New account created: {self.account_number}")
                return True
                
        except mysql.connector.Error as err:
            logger.error(f"Account creation error: {err}")
            print(f"Error creating account: {err}")
            return False
    
    def _validate_account_data(self) -> bool:
        """Validate account data before creation"""
        if not self.name or len(self.name) < 2:
            print("Please enter a valid name (minimum 2 characters).")
            return False
            
        if not self._validate_phone_number(self.phone):
            print("Please enter a valid phone number (10 digits starting with valid prefix).")
            return False
            
        return True
    
    def _phone_exists(self) -> bool:
        """Check if a phone number already exists in the database"""
        try:
            with DatabaseConnection() as (_, cursor):
                cursor.execute("SELECT id FROM bank WHERE phone = %s", (self.phone,))
                return cursor.fetchone() is not None
        except mysql.connector.Error as err:
            logger.error(f"Phone check error: {err}")
            return False
    
    @staticmethod
    def _validate_phone_number(phone: str) -> bool:
        """
        Validate a phone number format
        
        Args:
            phone: Phone number to validate
            
        Returns:
            bool: True if phone number is valid, False otherwise
        """
        if not phone:
            return False
            
        # UG phone format: 077, 078, 076, 070, 075 + 7 more digits
        pattern = r'^(077|078|076|070|075)\d{7}$'
        return bool(re.match(pattern, phone))
    
    def login(self, account_number: str, pin: str) -> bool:
        """
        Authenticate user login
        
        Args:
            account_number: Account number
            pin: PIN code
            
        Returns:
            bool: True if login successful, False otherwise
        """
        if self.login_attempts >= self.MAX_LOGIN_ATTEMPTS:
            print("\033[91mToo many failed login attempts. Please try again later.\033[0m")
            logger.warning(f"Account locked due to too many failed attempts: {account_number}")
            return False
            
        try:
            with DatabaseConnection() as (conn, cursor):
                cursor.execute(
                    "SELECT name, phone, pin, account_number, balance FROM bank WHERE account_number = %s",
                    (account_number,)
                )
                data = cursor.fetchone()
                
                if not data:
                    print("Account number does not exist")
                    self.login_attempts += 1
                    return False
                    
                # Verify hashed PIN
                hashed_pin = self._hash_pin(pin)
                if hashed_pin != data[2]:
                    self.login_attempts += 1
                    remaining = self.MAX_LOGIN_ATTEMPTS - self.login_attempts
                    print(f"\033[91mIncorrect PIN. {remaining} attempts remaining.\033[0m")
                    return False
                
                # Update login info
                self.name = data[0]
                self.phone = data[1]
                self.account_number_login = data[3]
                self.balance = float(data[4])
                
                # Reset login attempts and update last login time
                self.login_attempts = 0
                cursor.execute(
                    "UPDATE bank SET last_login = CURRENT_TIMESTAMP WHERE account_number = %s",
                    (account_number,)
                )
                conn.commit()
                
                print(f"\033[92mWelcome back, {self.name}!\033[0m")
                logger.info(f"Successful login: {account_number}")
                return True
                
        except mysql.connector.Error as err:
            logger.error(f"Login error: {err}")
            print("Login failed due to a system error.")
            return False
    
    def deposit(self, amount: float) -> bool:
        """
        Deposit money into account
        
        Args:
            amount: Amount to deposit
            
        Returns:
            bool: True if deposit successful, False otherwise
        """
        if not self._is_logged_in():
            return False
            
        if not self._validate_amount(amount):
            return False
            
        try:
            self.balance += amount
            self._update_account("deposit", amount)
            print(f"\033[92mDeposit of ${amount:.2f} successful\033[0m")
            self.check_balance()
            logger.info(f"Deposit: {self.account_number_login}, Amount: {amount}")
            return True
        except Exception as e:
            logger.error(f"Deposit error: {e}")
            print("Transaction failed. Please try again.")
            return False
    
    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from account
        
        Args:
            amount: Amount to withdraw
            
        Returns:
            bool: True if withdrawal successful, False otherwise
        """
        if not self._is_logged_in():
            return False
            
        if not self._validate_amount(amount):
            return False
            
        # Get current balance from database to avoid race conditions
        current_balance = self._get_current_balance()
        
        if amount > current_balance:
            print(f"\033[91mInsufficient balance. Your current balance is ${current_balance:.2f}\033[0m")
            return False
            
        try:
            self.balance = current_balance - amount
            self._update_account("withdraw", amount)
            print(f"\033[92mWithdrawal of ${amount:.2f} successful\033[0m")
            self.check_balance()
            logger.info(f"Withdrawal: {self.account_number_login}, Amount: {amount}")
            return True
        except Exception as e:
            logger.error(f"Withdrawal error: {e}")
            print("Transaction failed. Please try again.")
            return False
    
    def transfer(self, amount: float, recipient_account: str) -> bool:
        """
        Transfer money to another account
        
        Args:
            amount: Amount to transfer
            recipient_account: Recipient account number
            
        Returns:
            bool: True if transfer successful, False otherwise
        """
        if not self._is_logged_in():
            return False
            
        if not self._validate_amount(amount):
            return False
            
        # Validate recipient account
        if not self._validate_recipient(recipient_account):
            return False
            
        # Get current balance to avoid race conditions
        current_balance = self._get_current_balance()
        
        if amount > current_balance:
            print(f"\033[91mInsufficient balance. Your current balance is ${current_balance:.2f}\033[0m")
            return False
            
        try:
            # Use transaction to ensure atomicity
            with DatabaseConnection() as (conn, cursor):
                # Start transaction
                conn.start_transaction()
                
                # Deduct from sender
                self.balance = current_balance - amount
                cursor.execute(
                    "UPDATE bank SET balance = %s WHERE account_number = %s",
                    (self.balance, self.account_number_login)
                )
                
                # Add to recipient
                cursor.execute(
                    "UPDATE bank SET balance = balance + %s WHERE account_number = %s",
                    (amount, recipient_account)
                )
                
                # Record outgoing transaction
                cursor.execute(
                    "INSERT INTO transactions (account_number, transaction_type, amount, recipient_account) "
                    "VALUES (%s, %s, %s, %s)",
                    (self.account_number_login, "transfer_out", amount, recipient_account)
                )
                
                # Record incoming transaction
                cursor.execute(
                    "INSERT INTO transactions (account_number, transaction_type, amount, recipient_account) "
                    "VALUES (%s, %s, %s, %s)",
                    (recipient_account, "transfer_in", amount, self.account_number_login)
                )
                
                # Commit transaction
                conn.commit()
                
                print(f"\033[92mTransfer of ${amount:.2f} to account {recipient_account} successful\033[0m")
                self.check_balance()
                logger.info(f"Transfer: {self.account_number_login} -> {recipient_account}, Amount: {amount}")
                return True
                
        except mysql.connector.Error as err:
            logger.error(f"Transfer error: {err}")
            print("Transfer failed. Please try again.")
            return False
    
    def _validate_recipient(self, recipient_account: str) -> bool:
        """Validate recipient account for transfers"""
        if recipient_account == self.account_number_login:
            print("You cannot transfer to your own account")
            return False
            
        try:
            with DatabaseConnection() as (_, cursor):
                cursor.execute(
                    "SELECT account_number FROM bank WHERE account_number = %s",
                    (recipient_account,)
                )
                if not cursor.fetchone():
                    print("Recipient account number does not exist")
                    return False
                return True
        except mysql.connector.Error as err:
            logger.error(f"Recipient validation error: {err}")
            print("Error validating recipient account")
            return False
    
    def _update_account(self, transaction_type: str, amount: float, recipient_account: str = None) -> None:
        """Update account balance and transaction history"""
        try:
            with DatabaseConnection() as (conn, cursor):
                # Update balance
                cursor.execute(
                    "UPDATE bank SET balance = %s WHERE account_number = %s",
                    (self.balance, self.account_number_login)
                )
                
                # Record transaction
                cursor.execute(
                    "INSERT INTO transactions (account_number, transaction_type, amount, recipient_account) "
                    "VALUES (%s, %s, %s, %s)",
                    (self.account_number_login, transaction_type, amount, recipient_account)
                )
                
                conn.commit()
                
        except mysql.connector.Error as err:
            logger.error(f"Account update error: {err}")
            raise Exception(f"Failed to update account: {err}")
    
    def check_balance(self) -> float:
        """
        Check account balance
        
        Returns:
            float: Current account balance
        """
        if not self._is_logged_in():
            return 0.0
            
        balance = self._get_current_balance()
        print(f"Your current balance is: \033[1m${balance:.2f}\033[0m")
        return balance
    
    def _get_current_balance(self) -> float:
        """Get current balance from database"""
        try:
            with DatabaseConnection() as (_, cursor):
                cursor.execute(
                    "SELECT balance FROM bank WHERE account_number = %s",
                    (self.account_number_login,)
                )
                data = cursor.fetchone()
                return float(data[0]) if data else 0.0
        except mysql.connector.Error as err:
            logger.error(f"Balance check error: {err}")
            raise Exception(f"Failed to check balance: {err}")
    
    def check_transaction_history(self, limit: int = 10) -> List[Dict]:
        """
        Check transaction history
        
        Args:
            limit: Maximum number of transactions to return
            
        Returns:
            List[Dict]: List of transactions
        """
        if not self._is_logged_in():
            return []
            
        try:
            with DatabaseConnection() as (_, cursor):
                cursor.execute(
                    "SELECT transaction_type, amount, recipient_account, date "
                    "FROM transactions WHERE account_number = %s "
                    "ORDER BY date DESC LIMIT %s",
                    (self.account_number_login, limit)
                )
                
                transactions = []
                print("\n\033[1mYour recent transaction history:\033[0m")
                print("-" * 60)
                print(f"{'Type':<15} {'Amount':<10} {'Date':<20} {'Details':<20}")
                print("-" * 60)
                
                for row in cursor.fetchall():
                    trans_type, amount, recipient, date = row
                    transactions.append({
                        "type": trans_type,
                        "amount": float(amount),
                        "recipient": recipient,
                        "date": date
                    })
                    
                    # Format transaction for display
                    type_display = {
                        "deposit": "Deposit",
                        "withdraw": "Withdrawal",
                        "transfer_out": "Transfer Out",
                        "transfer_in": "Transfer In"
                    }.get(trans_type, trans_type)
                    
                    details = f"To: {recipient}" if recipient and trans_type == "transfer_out" else \
                              f"From: {recipient}" if recipient and trans_type == "transfer_in" else ""
                    
                    print(f"{type_display:<15} ${amount:<9.2f} {date.strftime('%Y-%m-%d %H:%M'):<20} {details:<20}")
                
                print("-" * 60)
                return transactions
                
        except mysql.connector.Error as err:
            logger.error(f"Transaction history error: {err}")
            print("Failed to retrieve transaction history")
            return []
    
    def _is_logged_in(self) -> bool:
        """Check if user is logged in"""
        if not self.account_number_login:
            print("You must be logged in to perform this action")
            return False
        return True
    
    def _validate_amount(self, amount: float) -> bool:
        """Validate transaction amount"""
        if amount <= 0:
            print("Amount must be greater than zero")
            return False
            
        if amount > 1000000:  # Example limit
            print("Amount exceeds transaction limit")
            return False
            
        return True


class BankUI:
    """
    User interface for bank system
    """
    def __init__(self):
        self.bank = None
    
    def clear_screen(self, delay: int = 0):
        """Clear terminal screen after optional delay"""
        if delay:
            sleep(delay)
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self, title: str):
        """Print formatted header"""
        width = 50
        print("\n" + "=" * width)
        print(f"{title.center(width)}")
        print("=" * width + "\n")
    
    def main_menu(self):
        """Display main menu"""
        self.clear_screen()
        self.print_header("BANKING SYSTEM")
        
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        
        while True:
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == '1':
                self.create_account_menu()
                break
            elif choice == '2':
                self.login_menu()
                break
            elif choice == '3':
                self.exit_system()
                break
            else:
                print("Invalid choice. Please try again.")
    
    def create_account_menu(self):
        """Display account creation menu"""
        self.clear_screen()
        self.print_header("CREATE NEW ACCOUNT")
        
        try:
            name = input("Enter your name: ").strip()
            phone = input("Enter your phone number: ").strip()
            
            # PIN input with masking
            pin = getpass.getpass("Enter your PIN (will be hidden): ")
            pin_confirm = getpass.getpass("Confirm your PIN: ")
            
            if pin != pin_confirm:
                print("\n\033[91mPINs do not match!\033[0m")
                input("\nPress Enter to try again...")
                self.create_account_menu()
                return
                
            # Create bank instance and account
            self.bank = Bank(name, phone, pin)
            if self.bank.create_account():
                input("\nPress Enter to continue to login...")
                self.login_menu()
            else:
                input("\nPress Enter to return to main menu...")
                self.main_menu()
                
        except KeyboardInterrupt:
            print("\n\nOperation cancelled")
            self.main_menu()
    
    def login_menu(self):
        """Display login menu"""
        self.clear_screen()
        self.print_header("ACCOUNT LOGIN")
        
        try:
            account_number = input("Enter your account number: ").strip()
            pin = getpass.getpass("Enter your PIN (will be hidden): ")
            
            self.bank = Bank()
            if self.bank.login(account_number, pin):
                self.account_menu()
            else:
                input("\nPress Enter to return to main menu...")
                self.main_menu()
                
        except KeyboardInterrupt:
            print("\n\nOperation cancelled")
            self.main_menu()
    
    def account_menu(self):
        """Display account menu after successful login"""
        while True:
            self.clear_screen()
            self.print_header(f"WELCOME, {self.bank.name.upper()}")
            
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Logout")
            
            try:
                choice = input("\nEnter your choice (1-6): ")
                
                if choice == '1':
                    self.deposit_menu()
                elif choice == '2':
                    self.withdraw_menu()
                elif choice == '3':
                    self.transfer_menu()
                elif choice == '4':
                    self.balance_menu()
                elif choice == '5':
                    self.history_menu()
                elif choice == '6':
                    print("\nLogging out...")
                    self.main_menu()
                    break
                else:
                    print("Invalid choice. Please try again.")
                    input("\nPress Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\nOperation cancelled")
                continue
    
    def deposit_menu(self):
        """Handle deposit operation"""
        self.clear_screen()
        self.print_header("DEPOSIT FUNDS")
        
        try:
            amount_str = input("Enter amount to deposit: $").strip()
            try:
                amount = float(amount_str)
                self.bank.deposit(amount)
            except ValueError:
                print("\033[91mInvalid amount. Please enter a numeric value.\033[0m")
                
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:
            print("\n\nOperation cancelled")
    
    def withdraw_menu(self):
        """Handle withdrawal operation"""
        self.clear_screen()
        self.print_header("WITHDRAW FUNDS")
        
        try:
            amount_str = input("Enter amount to withdraw: $").strip()
            try:
                amount = float(amount_str)
                self.bank.withdraw(amount)
            except ValueError:
                print("\033[91mInvalid amount. Please enter a numeric value.\033[0m")
                
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:
            print("\n\nOperation cancelled")
    
    def transfer_menu(self):
        """Handle transfer operation"""
        self.clear_screen()
        self.print_header("TRANSFER FUNDS")
        
        try:
            recipient = input("Enter recipient account number: ").strip()
            amount_str = input("Enter amount to transfer: $").strip()
            
            try:
                amount = float(amount_str)
                self.bank.transfer(amount, recipient)
            except ValueError:
                print("\033[91mInvalid amount. Please enter a numeric value.\033[0m")
                
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:
            print("\n\nOperation cancelled")
    
    def balance_menu(self):
        """Display account balance"""
        self.clear_screen()
        self.print_header("ACCOUNT BALANCE")
        
        self.bank.check_balance()
        input("\nPress Enter to continue...")
    
    def history_menu(self):
        """Display transaction history"""
        self.clear_screen()
        self.print_header("TRANSACTION HISTORY")
        
        self.bank.check_transaction_history()
        input("\nPress Enter to continue...")
    
    def exit_system(self):
        """Exit the banking system"""
        self.clear_screen()
        print("\n\033[92mThank you for using our banking system. Goodbye!\033[0m\n")
        sys.exit(0)


if __name__ == '__main__':
    # Create .env file if it doesn't exist
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write("DB_HOST=localhost\n")
            f.write("DB_USER=root\n")
            f.write("DB_PASSWORD=\n")
            f.write("DB_NAME=bank\n")
            f.write("PIN_SALT=MY_SECRET_SALT\n")
        
    try:
        ui = BankUI()
        ui.main_menu()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user")
    except Exception as e:
        logger.critical(f"Unhandled exception: {e}")
        print(f"\n\033[91mAn unexpected error occurred: {e}\033[0m")
        print("Check the log file for details.")
