class Bank:
    def __init__(self, customerID):
        self.ID = customerID
        print self
        self.total = 0

    def deposit(self, amount):
        self.total = self.total + amount
        return self.total

    def withdraw(self, amount):
        self.total = self.total - amount
        return self.total

    def balance(self):
        return self.total

    def transfer(self, amount, ID):
        self.total = self.total - amount
        print ID
        ID.total = ID.total + amount
        print ID.total
        return ID.balance()

bank1 = Bank(111)
print bank1.deposit(150)
bank2 = Bank(222)
print bank1.transfer(50, bank2)
