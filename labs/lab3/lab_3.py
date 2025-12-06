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

    def save_statement(self, client_id, filename=None):
        if client_id not in self.clients:
            raise ValueError("Клиент не найден")

        client = self.clients[client_id]

        if filename is None:
            filename = f"bank_statement_{client_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        total_balance = 0
        statement_data = {
            'client_id': client_id,
            'client_name': client.name,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'accounts': [],
            'total_balance': 0
        }

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"ВЫПИСКА ПО СЧЕТАМ\n")
            f.write(f"Банк: {self.name}\n")
            f.write(f"Клиент: {client.name} (ID: {client_id})\n")
            f.write(f"Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 50 + "\n\n")

            for currency, account in client.accounts.items():
                status = "Активен" if account.is_active else "Закрыт"
                f.write(f"Счет: {account.account_number}\n")
                f.write(f"Валюта: {currency}\n")
                f.write(f"Баланс: {account.balance:.2f} {currency}\n")
                f.write(f"Статус: {status}\n")
                f.write(f"Дата открытия: {account.created_date.strftime('%Y-%m-%d')}\n")
                f.write("-" * 30 + "\n")

                statement_data['accounts'].append({
                    'account_number': account.account_number,
                    'currency': currency,
                    'balance': account.balance,
                    'status': status
                })
                total_balance += account.balance

            f.write(f"\nОБЩИЙ БАЛАНС: {total_balance:.2f}\n")
            statement_data['total_balance'] = total_balance

        # Сохраняем также в JSON для машиночитаемого формата
        json_filename = filename.replace('.txt', '.json')
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(statement_data, f, ensure_ascii=False, indent=2)

        return filename


def main():
    bank = Bank("Наш Банк")

    # Создаем тестовых клиентов
    try:
        bank.register_client("001", "Иван Иванов", "+79161234567", "ivan@mail.com")
        bank.register_client("002", "Мария Петрова", "+79167654321", "maria@mail.com")

        bank.open_account("001", "RUB", 1000)
        bank.open_account("001", "USD", 500)
        bank.open_account("002", "RUB", 2000)
    except ValueError as e:
        pass

    current_client = None

    while True:
        print("\n" + "=" * 50)
        print("БАНКОВСКАЯ СИСТЕМА")
        print("=" * 50)

        if current_client is None:
            print("1. Войти в систему")
            print("2. Зарегистрироваться")
            print("3. Выйти")
        else:
            print(f"Добро пожаловать, {bank.clients[current_client].name}!")
            print("1. Открыть счет")
            print("2. Закрыть счет")
            print("3. Пополнить счет")
            print("4. Снять со счета")
            print("5. Перевести деньги")
            print("6. Выписка по счетам")
            print("7. Информация о счетах")
            print("8. Выйти из системы")

        choice = input("Выберите действие: ")

        try:
            if current_client is None:
                if choice == "1":
                    client_id = input("Введите ваш ID: ")
                    if client_id in bank.clients:
                        current_client = client_id
                        print("Успешный вход!")
                    else:
                        print("Клиент не найден!")

                elif choice == "2":
                    client_id = input("Введите ID: ")
                    name = input("Введите ФИО: ")
                    phone = input("Введите телефон: ")
                    email = input("Введите email: ")

                    bank.register_client(client_id, name, phone, email)
                    current_client = client_id
                    print("Регистрация успешна!")

                elif choice == "3":
                    print("До свидания!")
                    break

                else:
                    print("Неверный выбор!")

            else:
                if choice == "1":
                    currency = input("Введите валюту счета (RUB, USD, EUR): ").upper()
                    initial_balance = float(input("Начальный баланс: "))

                    account = bank.open_account(current_client, currency, initial_balance)
                    print(f"Счет открыт! Номер счета: {account.account_number}")

                elif choice == "2":
                    currency = input("Введите валюту счета для закрытия: ").upper()
                    bank.close_account(current_client, currency)
                    print("Счет закрыт!")

                elif choice == "3":
                    currency = input("Введите валюту счета: ").upper()
                    amount = float(input("Сумма пополнения: "))

                    account = bank.get_client_accounts_info(current_client)[currency]
                    account.deposit(amount)
                    print(f"Счет пополнен! Новый баланс: {account.balance} {currency}")

                elif choice == "4":
                    currency = input("Введите валюту счета: ").upper()
                    amount = float(input("Сумма снятия: "))

                    account = bank.get_client_accounts_info(current_client)[currency]
                    account.withdraw(amount)
                    print(f"Снятие успешно! Новый баланс: {account.balance} {currency}")

                elif choice == "5":
                    from_currency = input("Ваша валюта для перевода: ").upper()
                    to_client_id = input("ID получателя: ")
                    to_currency = input("Валюта получателя: ").upper()
                    amount = float(input("Сумма перевода: "))

                    bank.transfer(current_client, from_currency, to_client_id, to_currency, amount)
                    print("Перевод выполнен успешно!")

                elif choice == "6":
                    filename = bank.save_statement(current_client)
                    print(f"Выписка сохранена в файл: {filename}")

                elif choice == "7":
                    accounts = bank.get_client_accounts_info(current_client)
                    print("\nВАШИ СЧЕТА:")
                    for currency, account in accounts.items():
                        status = "Активен" if account.is_active else "Закрыт"
                        print(f"{currency}: {account.balance:.2f} ({status})")

                elif choice == "8":
                    current_client = None
                    print("Выход из системы...")

                else:
                    print("Неверный выбор!")

        except ValueError as e:
            print(f"Ошибка: {e}")
        except KeyError as e:
            print(f"Ошибка: Счет не найден")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")


if __name__ == "__main__":
    main()