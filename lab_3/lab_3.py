import json
from datetime import datetime


class Client:
    def __init__(self, client_id, name, phone, email):
        self.client_id = client_id
        self.name = name
        self.phone = phone
        self.email = email
        self.accounts = {}  # currency -> BankAccount


class BankAccount:
    def __init__(self, account_number, client, currency, initial_balance=0):
        self.account_number = account_number
        self.client = client
        self.currency = currency
        self.balance = initial_balance
        self.is_active = True
        self.created_date = datetime.now()
        self.transactions = []

    def deposit(self, amount):
        if not self.is_active:
            raise ValueError("Счет закрыт")
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")

        self.balance += amount
        self.transactions.append(f"{datetime.now()}: Пополнение +{amount} {self.currency}")

    def withdraw(self, amount):
        if not self.is_active:
            raise ValueError("Счет закрыт")
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")

        self.balance -= amount
        self.transactions.append(f"{datetime.now()}: Снятие -{amount} {self.currency}")

    def close_account(self):
        if self.balance != 0:
            raise ValueError("Невозможно закрыть счет с ненулевым балансом")
        self.is_active = False


class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = {}  # client_id -> Client
        self.accounts = {}  # account_number -> BankAccount
        self.account_counter = 1

    def register_client(self, client_id, name, phone, email):
        if client_id in self.clients:
            raise ValueError("Клиент с таким ID уже существует")

        client = Client(client_id, name, phone, email)
        self.clients[client_id] = client
        return client

    def open_account(self, client_id, currency, initial_balance=0):
        if client_id not in self.clients:
            raise ValueError("Клиент не найден")

        client = self.clients[client_id]

        if currency in client.accounts:
            raise ValueError(f"У клиента уже есть счет в валюте {currency}")

        account_number = f"ACC{self.account_counter:06d}"
        self.account_counter += 1

        account = BankAccount(account_number, client, currency, initial_balance)
        client.accounts[currency] = account
        self.accounts[account_number] = account

        return account

    def close_account(self, client_id, currency):
        if client_id not in self.clients:
            raise ValueError("Клиент не найден")

        client = self.clients[client_id]

        if currency not in client.accounts:
            raise ValueError(f"У клиента нет счета в валюте {currency}")

        account = client.accounts[currency]
        account.close_account()
        del client.accounts[currency]
        del self.accounts[account.account_number]

    def transfer(self, from_client_id, from_currency, to_client_id, to_currency, amount):
        if from_client_id not in self.clients:
            raise ValueError("Отправитель не найден")
        if to_client_id not in self.clients:
            raise ValueError("Получатель не найден")

        from_client = self.clients[from_client_id]
        to_client = self.clients[to_client_id]

        if from_currency not in from_client.accounts:
            raise ValueError(f"У отправителя нет счета в валюте {from_currency}")
        if to_currency not in to_client.accounts:
            raise ValueError(f"У получателя нет счета в валюте {to_currency}")

        from_account = from_client.accounts[from_currency]
        to_account = to_client.accounts[to_currency]

        # Снимаем с одного счета
        from_account.withdraw(amount)

        # Пополняем другой счет
        to_account.deposit(amount)

        # Записываем транзакции
        from_account.transactions.append(f"{datetime.now()}: Перевод {amount} {from_currency} клиенту {to_client_id}")
        to_account.transactions.append(f"{datetime.now()}: Перевод {amount} {to_currency} от клиента {from_client_id}")

    def get_client_accounts_info(self, client_id):
        if client_id not in self.clients:
            raise ValueError("Клиент не найден")

        client = self.clients[client_id]
        return client.accounts

