class User:
    
    #TODO Create a file with the User class, including the __init__ with all the attributes, parameters and default values.
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    #TODO display_info(self) - Have this method print all of the users' details on separate lines.
    def display_info(self):
        print(f"{self.first_name} \n{self.last_name} \n{self.email} \n{self.age}\nIs Rewards member:{self.is_rewards_member}\nGold Card Points: {self.gold_card_points}\n")
    
        return self
    #TODO enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self):
        if(self.is_rewards_member == True):
            print("User already a member")
            return self
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self
        
    
    #TODO spend_points(self, amount) - have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        if(self.gold_card_points > amount):
            self.gold_card_points -= amount
        else:
            print("Dont have enough points")
        return self
        
immanuel = User("Immanuel","Vattakunnel", "immanuelvatta@gmail.com",29)
# immanuel.display_info()
# immanuel.enroll()
# immanuel.display_info()

# #? Make 2 more instances of the User class.
john = User("John", "Smith", "johnsmith@example.com", 33)
# john.display_info()

jane = User("Jane", "Doe", "janedoe@abc.com", 32)
# jane.display_info()

# #? Have the first user spend 50 points
# immanuel.spend_points(50)
# immanuel.display_info()

# #? Have the second user enroll.
# john.enroll()

# #? Have the second user spend 80 points
# john.spend_points(80)
# john.display_info()

# #TODO Call the display method on all the users.

immanuel.display_info().enroll().spend_points(50).display_info()
john.enroll().spend_points(80).display_info()
jane.display_info()
# immanuel.display_info()
# john.display_info()
# jane.display_info()