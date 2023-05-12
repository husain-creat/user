class User():
    def __init__(self,name,email):
        self.name = name
        self.email = email 
        self.account_balance = 0      
    def make_deposit(self,amount):
        self.account_balance+=amount
        return self 
    def make_withdrawal(self,amount):
        self.account_balance-=amount
        return self
    def display_user_balance(self):
         print(self.name , self.account_balance)
         return self
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
guido.make_deposit(200).make_deposit(200).make_deposit(200).make_withdrawal(50).display_user_balance()
monty.make_deposit(300).make_deposit(300).make_withdrawal(100).make_withdrawal(100).display_user_balance()    