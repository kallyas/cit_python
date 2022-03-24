import sys
import os
from datetime import datetime, time
from time import sleep
import secrets
import hashlib
import mysql.connector
import re
from typing import Union

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
    def __init__(self, name: str, phone: str, pin: Union[int, str]):
        self.name = name
        self.phone = phone
        self.pin = hashlib.sha256(pin.encode()).hexdigest()
        self.account_number = self.generate_account_number()
        self.balance = 0
        self.account_number_login = ''
        self.login_try = 0
        # create database immediately when an instance of Bank is created
        self.create_database()

    def create_database(self):
        # create database
        conn, c = self.connect_db()
        c.execute('''CREATE TABLE IF NOT EXISTS bank (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), phone VARCHAR(255), pin VARCHAR(255), account_number VARCHAR(255) not null unique, balance INT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS transactions (id INT PRIMARY KEY AUTO_INCREMENT, account_number VARCHAR(255) not null, transaction_type VARCHAR(255) not null, amount INT not null, date DATETIME default CURRENT_TIMESTAMP)''')

        conn.commit()
        conn.close()
        print('Database created')

    def check_login_tries(self):
        if self.login_try == 3:
            print('You have exceeded the maximum number of login attempts')
            return False
        else:
            return True


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
        if amount <= self.get_balance():
            if self.transfer_to_account(account_number, amount):
                self.balance = self.get_balance() - amount
                self.update_database("transfer", amount)
                print('Transfer successful')
                self.check_balance()
        else:
            print('Insufficient balance')

    def transfer_to_account(self, account_number, amount):
        # transfer to another existing account
        conn, c = self.connect_db()
        # check if account number exists
        c.execute('''SELECT account_number, balance FROM bank WHERE account_number = %s''', (account_number,))
        data = c.fetchone()
        if data is None:
            print('Account number does not exist')
            return False
        else:
            # check if account number is not the same as the one logged in
            if data[0] == self.account_number_login:
                print('You cannot transfer to your own account')
                return False
            else:
                c.execute('''UPDATE bank SET balance = %s WHERE account_number = %s''', (data[1] + amount, account_number))
                conn.commit()
                conn.close()
                return True
        
        

    def check_balance(self):
        # check balance
        conn, c = self.connect_db()
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

    def login(self, account_number: str, pin: Union[int, str]):
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
            self.login_try = self.check_login_tries()
            if hashed_pin == data[3] and self.login_try:
                self.account_number_login = data[4]
                self.balance = data[5]
                print('Login successful')
                return True
            else:
                self.login_try += 1
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
        print('Thank you for using our bank')
        sys.exit()

# clear screen function
def clear():
    sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')


# UG phone format
# MTN: 077, 078, 076
# AIRTEL: 070, 075
# length: 10
def checkPhoneNumber(phone_number: str) -> bool:
    airtel_regex = re.compile(r'^(070|075)\d{7}$')
    mtn_regex = re.compile(r'^(077|078|076)\d{7}$')
    # check phone number
    if airtel_regex.search(phone_number) or mtn_regex.search(phone_number):
        return True
    else:
        return False

def main(Bank, clear):
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
        while not checkPhoneNumber(phone):
            print('Invalid phone number')
            phone = input('Enter your phone number: ')
        pin = input('Enter your pin: ')
        if not name or not phone or not pin:
            print('cannot create account. All fields are required')
            clear()
            exit()
        else:
            bank = Bank(name, phone, pin)
            bank.create_account()
    elif user_input == '2':
        account_number = input('Enter your account number: ')
        pin = input('Enter your pin: ')
        bank = Bank('', '', '')
        if bank.login(account_number, pin):
            while True:
                # clear()
                print('Welcome Back')
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
                    clear()
                elif user_input == '2':
                    amount = int(
                        input('Enter the amount you want to withdraw: '))
                    bank.withdraw(amount)
                    clear()
                elif user_input == '3':
                    amount = int(
                        input('Enter the amount you want to transfer: '))
                    account_number = input(
                        'Enter the account number you want to transfer to: ')
                    bank.transfer(amount, account_number)
                    clear()
                elif user_input == '4':
                    bank.check_balance()
                    clear()
                elif user_input == '5':
                    bank.check_history()
                    clear()
                elif user_input == '6':
                    bank.exit()
                else:
                    print('Invalid input')
        else:
            print('Login failed')
            clear()
    elif user_input == '3':
        sys.exit()
    else:
        print('Invalid input')
        sys.exit()

    

if __name__ == '__main__':
    # create 1st menu
    main(Bank, clear)