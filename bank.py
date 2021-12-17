import sys
import os
from datetime import datetime
import secrets
import hashlib
import mysql.connector

# Bank class
# user can create account, deposit, withdraw, transfer, check balance, check history, and exit
# user can only withdraw if they have enough money in their account
# user can only transfer if they have enough money in their account
# user has name, phone number, pin
# account number is generated automatically
# user details and transaction history are stored in mysql database
# user can only access their own account
# user can only access their own transaction history
# user can only access their own account number
# user details are entered by user


class Bank:
    def __init__(self, name, phone, pin):
        self.name = name
        self.phone = phone
        self.pin = hashlib.sha256(pin.encode()).hexdigest()
        self.account_number = self.generate_account_number()
        self.balance = 0
        self.account_number_login = ''
        # create database immediately when an instance of Bank is created
        self.create_database()

    def create_database(self):
        # create database
        conn, c = self.connect_db()
        c.execute('''CREATE TABLE IF NOT EXISTS bank (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), phone VARCHAR(255), pin VARCHAR(255), account_number VARCHAR(255), balance INT)''')
        conn.commit()
        conn.close()
        print('Database created')

    def generate_account_number(self):
        # account number format: AC+last 4 digits of phone number+current date+random number and account number max length 15
        account_number = 'AC' + \
            self.phone[-4:] + datetime.now().strftime('%Y%m%d') + \
            str(secrets.randbits(15))
        return account_number

    def create_account(self):
        # create account
        conn, c = self.connect_db()
        sql = ("INSERT INTO bank (name, phone, pin, account_number, balance)"
               "VALUES (%s, %s, %s, %s, %s)"
               )
        data = (self.name, self.phone, self.pin, self.account_number,
                self.balance)

        try:
            c.execute(sql, data)
            conn.commit()
            print('Account created')
            print('Your account number is: ' + self.account_number)
        except mysql.connector.Error as err:
            print('Error' + str(err))
            conn.rollback()
        conn.close()

    def deposit(self, amount):
        # deposit money
        self.balance = self.get_balance() + amount
        self.update_database("deposit", amount)
        print('Deposit successful')
        self.check_balance()

    def withdraw(self, amount):
        # withdraw money
        if amount <= self.balance:
            self.balance = self.get_balance() - amount
            self.update_database("withdraw", amount)
            print('Withdraw successful')
            self.check_balance()
        else:
            print('Insufficient balance')

    def transfer(self, amount, account_number):
        # transfer money to another account
        if amount <= self.balance:
            self.balance = self.get_balance() - amount
            self.update_database("transfer", amount)
            print('Transfer successful')
            self.check_balance()
        else:
            print('Insufficient balance')

    def check_balance(self):
        # check balance
        conn, c = self.connect_db()
        c = conn.cursor()
        c.execute('''SELECT balance FROM bank WHERE account_number = %s''', (self.account_number_login,))
        data = c.fetchone()
        conn.close()
        print('Your current balance is: ' + str(data[0]))

    def check_history(self):
       conn, c = self.connect_db()
       c.execute('''SELECT * FROM transactions WHERE account_number = %s''', (self.account_number_login,))
       data = c.fetchall()
       conn.close()
       print('Your transaction history:')
       for row in data:
        print(row[2] + ' of $' + str(row[3]) + ' on ' + str(row[4]))


    def get_balance(self ):
        conn, c = self.connect_db()
        c.execute('''SELECT balance FROM bank WHERE account_number = %s''', (self.account_number_login,))
        data = c.fetchone()
        conn.close()
        return data[0]

    def update_database(self, t_type, amount):
        # update database
        conn, c = self.connect_db()
        c.execute('''UPDATE bank SET balance = %s WHERE account_number = %s''',
                  (self.balance, self.account_number_login))
        c.execute('''INSERT INTO transactions (account_number, transaction_type, amount) VALUES (%s, %s, %s)''',
                    (self.account_number_login, t_type, amount))
        conn.commit()
        conn.close()
        print('Database updated')

    def login(self, account_number, pin):
        # login
        conn, c = self.connect_db()
        c.execute('''SELECT * FROM bank WHERE account_number = %s''',
                  (account_number,))
        data = c.fetchone()
        conn.close()

        if data is None:
            print('Account number does not exist')
        else:
            # hash pin and compare with database
            hashed_pin = hashlib.sha256(pin.encode()).hexdigest()
            if hashed_pin == data[3]:
                self.account_number_login = data[4]
                print('Login successful')
                return True
            else:
                print('Incorrect pin')
                return False

    def connect_db(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='bank'
        )
        c = conn.cursor()
        return conn, c

    def exit(self):
        # exit
        sys.exit()


if __name__ == '__main__':
    # create 1st menu
    print('Welcome to the Bank')
    print('1. Create account')
    print('2. Login')
    print('3. Exit')
    # get user input
    user_input = input('Enter your choice: ')
    # create 2nd menu
    if user_input == '1':
        name = input('Enter your name: ')
        phone = input('Enter your phone number: ')
        pin = input('Enter your pin: ')
        bank = Bank(name, phone, pin)
        bank.create_account()
    elif user_input == '2':
        account_number = input('Enter your account number: ')
        pin = input('Enter your pin: ')
        bank = Bank('', '', '')
        if bank.login(account_number, pin):
            while True:
                print('1. Deposit')
                print('2. Withdraw')
                print('3. Transfer')
                print('4. Check balance')
                print('5. Check history')
                print('6. Exit')
                user_input = input('Enter your choice: ')
                if user_input == '1':
                    amount = int(
                        input('Enter the amount you want to deposit: '))
                    bank.deposit(amount)
                elif user_input == '2':
                    amount = int(
                        input('Enter the amount you want to withdraw: '))
                    bank.withdraw(amount)
                elif user_input == '3':
                    amount = int(
                        input('Enter the amount you want to transfer: '))
                    account_number = input(
                        'Enter the account number you want to transfer to: ')
                    bank.transfer(amount, account_number)
                elif user_input == '4':
                    bank.check_balance()
                elif user_input == '5':
                    bank.check_history()
                elif user_input == '6':
                    bank.exit()
                else:
                    print('Invalid input')
        else:
            print('Login failed')
    elif user_input == '3':
        sys.exit()
    else:
        print('Invalid input')
        sys.exit()
