
#declare a class and give it name User
class Person:
    # ! CONSTRUCTION FUNCTION!!!! CREATES THE INSTANCE OF AN OBJECT
    def __init__(self):
        self.first_name = "Immanuel"
        self.last_name = "Vattakunnel"
        self.age = 29

# Now that you have a class set up with a constructor 
# You can assign new variables to new users in the outer scope!

#to invoke the innit function
user_immanuel = Person()
print(user_immanuel.first_name)

user_2 = Person()
print(user_2.first_name) #also prints Immanuel

class Shoe:
    # pass
    #TODO now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
        #! we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        
        # * the status is set to True by default
        self.in_stock = True
        
        
    def on_sale_by_percent(self, percent):
        self.price = self.price* (1 - percent)
    
    def total_with_tax (self, tax_rate):
        tax = self.price * tax_rate
        total = self.price + tax
        return total
    
    def cut_price_by(self, amount):
        if  amount < self.price:
            self.price -= amount
        else:
            print("Price deduction too large.")
    
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
basketball_shoe = Shoe("Nike", "Air-Force 1", 110.99)
my_shoe = Shoe("Converse", "Low-tops", 36.00)

print(my_shoe.total_with_tax(0.08))

my_shoe.cut_price_by(20.00)
print(my_shoe.price)
print(my_shoe.total_with_tax(0.08))
print(skater_shoe.type) #? output: Low-top Trainers
print(dress_shoe.brand) #? output: Jack & Jill Bootery 

basketball_shoe.in_stock = False
print(basketball_shoe.in_stock)

    

skater_shoe.on_sale_by_percent(0.2)
dress_shoe.on_sale_by_percent(0.5)
print(skater_shoe.price)
print(dress_shoe.price)
        
# #TODO The Skater shoes go on sale by 20% reduced price:
# skater_shoe.price = skater_shoe.price * (1 - 0.2)
# #TODO The dress shoe go on sale by 10% reduction:
# dress_shoe.price = dress_shoe.price * (1-0.1)
# #TODO The skater go on sale AGAIN by another 10%:
# skater_shoe.price = skater_shoe.price * (1-0.1)      



class User:
    
    
    #! CONSTRUCTOR FUNCTION!!!! CREATES THE INSTANCE OF AN OBJECT
    
    def __init__(self,first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        
    def greeting(self):
        print(f"Hello my name is {self.first_name} and my email is {self.email}!")

#!implementing a user    
immanuel = User("Immanuel","Vattakunnel",29, "immanuelvatta@gmail.com")
immanuel.greeting()