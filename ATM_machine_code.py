#Account operations :
class Account:
    def __init__(self,balance):
        self.balance = balance
        return

    def withdraw(self, amount):
        print("Withdrawing.... : ", amount)
        print("Avail balance : ", self.balance)
        if amount<=self.balance :
            self.balance = self.balance - amount
            print("Collect cash : ",amount)
        else:
            print("Low balance error")
        return

amount = int(input("Enter initial amount : "))
acc = Account(amount)
print("balance : ",acc.balance)
amount = int(input("Enter amount to withdraw : "))
acc.withdraw(amount)
print("Final balance : ", acc.balance)
