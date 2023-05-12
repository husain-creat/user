class User():
    def __init__(self,name,email):
        self.name = name
        self.email = email 
        self.account_balance = 0      
    def make_deposite(self,amount):
        self.account_balance+=amount 
    def make_withdrawal(self,amount):
        self.account_balance-=amount
    def display_user_balance(self):
         print(self.name , self.account_balance)
    
             
    
        
        
        
        
            
        
        
        
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	
print(monty.name) 
guido.make_deposite(1500)
guido.make_withdrawal(500)
guido.display_user_balance()











        
        

   



    


