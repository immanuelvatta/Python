from bank_account import BankAccount

class User:
    
    #! Constructor function !! Creates the instance of an object
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        # print(self.account.balance)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        # print(self.account.balance)

        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")
        return self


immanuel = User("Immanuel","immanuelvatta@gmail.com")
immanuel.display_user_balance().make_deposit(500).display_user_balance().make_withdrawal(300).display_user_balance()

