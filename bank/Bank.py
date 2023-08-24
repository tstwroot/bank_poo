from datetime import date

class Operation:
    def __init__(self):
        self.__operations = []

    @property
    def operations(self):
        return self.__operations
    
    @operations.setter
    def operations(self, operation:str):
        operation = operation + " || " + str(date.today())
        self.__operations.append(operation)
        return

class Bank(Operation):
    def __init__(self, bank_name:str, bank_address:str):
        Operation.__init__(self)
        self.__bank_name = bank_name
        self.__bank_address = bank_address
        self.__accounts = []
    
    def __repr__(self) -> None:
        return f"Bank Name: {self.__bank_name}\nBank Address: {self.__bank_address}"

    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, account:"Account"):
        self.__accounts.append(account)

class Client:
    def __init__(self, name:str, cpf:str, date:date) -> None:
        self.__name = name
        self.__cpf = cpf
        self.__date = date
        return
    
    def __repr__(self) -> None:
        return f"Name: {self.__name}\nCPF: {self.__cpf}\nDate: {self.__date}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        self.__date = date
    
class Account():
    def __init__(self, agency:str, account_number:int, balance:float, client:"Client", bank:"Bank") -> None:
        self.__agency = agency
        self.__account_number = account_number
        self.__balance = balance
        self.__initial_limit = 500
        self.__limit = self.__balance + self.__initial_limit
        self.__client = client;
        self.__bank = bank
        self.__bank.accounts = self
        return
    
    def __repr__(self) -> None:
        return f"Agency: {self.__agency}\nAccount Number: {self.__account_number}\nClient: {self.__client}\nBank: {self.__bank}"
    
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value:int) -> None:
        self.__balance += value
        return
    
    @property
    def limit(self):
        return self.__limit
    
    @limit.setter
    def limit(self, value:int):
        self.__limit = value

    def deposit(self, value:int) -> None:
        self.__balance += value
        self.__bank.operations = f"DEPOSIT: ({self.__agency} - {self.__account_number}) VALUE: {value}"
        return

    def to_withdraw(self, value:int) -> None:
        if(self.__limit - value < 0):
            print("Error: Can not withdraw your money, your limit are insuficient.")
            return
        
        self.__limit -= value
        self.__balance -= value
        print(f"Voce sacou: R$ {value}")
    
    def transfer(self, value:int, destination:"Account") -> None:
        if(self.__limit - value < 0):
            print("Error: Can not transfer your money to associated account, your limit are insuficient.")
            return
        
        self.__limit -= value
        self.__balance -= value
        destination.__balance += value
        self.__bank.operations = f"TRANSFER: ({self.__agency} - {self.__account_number} TO {destination.__agency} - {destination.__account_number}) VALUE: {value}"
        destination.__bank.operations = f"TRANSFER: ({self.__agency} - {self.__account_number} TO {destination.__agency} - {destination.__account_number}) VALUE: {value}"
        return