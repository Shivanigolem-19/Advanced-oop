# __init__
# __balance
# get_balance()
# set_balance(balance)
# if balance >= 0
# Object creation
# Change balance to 8000
# Try -500

class BankAccount():

    def __init__(self):
        self.__balance =5000

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("invalid")

Bank = BankAccount()

print(Bank.get_balance())

Bank.set_balance(8000)

print(Bank.get_balance())

Bank.set_balance(-500)

print(Bank.get_balance)
