import Bank
from datetime import date

if __name__ == "__main__":
    bank = Bank.Bank("Banco Nacional", "Rua Piririn Pororon, 2222")

    client1 = Bank.Client("João Silva", "123.456.789-00", date(1985, 5, 15))
    account1 = Bank.Account("001", "12345-6", 1000.0, client1, bank)

    print(account1)

    # account1.deposit(500.0)
    account1.balance = 500.0
    print(account1.balance)

    client2 = Bank.Client("Maria Souza", "987.654.321-00", date(1990, 10, 8))
    account2 = Bank.Account("002", "98765-4", 1500.0, client2, bank)

    account1.transfer(300.0, account2)

    print(account1.balance)
    print(account2.balance)

    print(bank.accounts)
    print(bank.operations)