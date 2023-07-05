class BankAccount:
    #! new class attribute - a list of all the accounts
    all_accounts = []
    
    #TODO Create a BankAccount class with the attributes interest rate and balance
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)


    #TODO Add a deposit method to the BankAccount class
    #TODO deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance +=amount
        
        return self

    #TODO Add a withdraw method to the BankAccount class
    #TODO withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; 
    #TODO if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            amount = 5
            print ("Insufficient funds: Charging a $5 fee")
            self.balance -= amount
        
        return self
    
    #! we can use the static method here to evaluate
    #! if we can withdraw the funds without going negative
    @staticmethod
    def can_withdraw(balance, amount):
        if ((balance-amount) < 0):
            return False
        else:
            return True
        
    #TODO Add a display_account_info method to the BankAccount class
    #TODO display_account_info(self) - print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    #TODO Add a yield_interest method to the BankAccount class
    #TODO yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if(self.balance > 0):
            
            self.balance += (self.balance * self.int_rate)
            return self
    
    #TODO NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
    #! class method to print all account balances
    @classmethod
    def all_balances(cls):
        for count,value in enumerate(cls.all_accounts, start=1):
            print(f"Balance of account {count}: {value.balance}")

#? Create 2 accounts
account1 = BankAccount(.05, 3000)
account2 = BankAccount(.10, 5000)

# account1.display_account_info()
#* To the first account, make 3 deposits and 1 withdrawal, then yield interest 
#* and display the account's info all in one line of code (i.e. chaining)
account1.deposit(500).deposit(200).deposit(400).withdraw(100).yield_interest().display_account_info()

#* To the second account, make 2 deposits and 4 withdrawals, 
#* then yield interest and display the account's info all in one line of code (i.e. chaining)
account2.deposit(300).deposit(150).withdraw(50).withdraw(510).withdraw(333).withdraw(155).yield_interest().display_account_info()

#? print all instances of a Bank Account's info
BankAccount.all_balances()