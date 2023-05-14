class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        return self    
class User:
    def __init__(self, name, email,int_rate,balance):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate, balance)
    
    def deposit(self):
        self.account.deposit(0)
        print(self.account.balance) 
    def withdraw(self):
        self.account.withdraw(0)
        print(self.account.balance)     
           
user1 = User("adf","dsakdjh@jh",.02,3000)


user1.account.deposit(300)
user1.account.withdraw(700)
print(user1.account.balance)



    
    	



    
