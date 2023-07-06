#blueprint -> defines what a User is

class User:
    all_users = []
    ceo = None #'billy bob'
    #! constructor method or magic method(all __ex__ methods)
    def __init__(self, first_name, last_name, age):
        #! attributes - the things that make up a class
        self.first_name = first_name#"Immanuel"
        self.last_name = last_name#"Vattakunnel"
        self.age =  age #29.
        User.all_users.append(self)
        
    #! method is a function inside a class
    #! The actions that a class can take
    def greetings(self):
        #normal method is going to act upn the "self"
        print(f"Hello my name is {self.first_name} {self.last_name} and I am {self.age} years old")
        return self
    
    def birthday(self):
        self.age += 1
        return self
    
    #give the average of the age of people in this list (not acting on the instance of a user)
    @classmethod
    def average_age(cls):
        #* acts upon the class
        #average = all ages added together / total number of people
        # print(cls.all_users)
        total_users = len(cls.all_users)
        # print(total_users)
        sum = 0
        for user in cls.all_users:
            print(user.age)
            sum += user.age
        average = (sum/total_users)
        return average
    
    @classmethod
    def change_ceo(cls, user):
        cls.ceo = user
        return cls
    # is over 21
    @staticmethod
    #* acts upon nothing. A normal function inside a class in order to encapsulate it with the class
    def check_age(user, age_to_check=21):
        if(user.age >= age_to_check):
            return True#("good to go")
        else:
            return False#("no good")
        
#! Creating an instance of the class
immanuel = User("Immanuel", "Vattakunnel", 28)
tom = User("Tom", "T", 22)
nick = User('nick','A',14)
billy_bob = User("billy", "bob", 55)
User.change_ceo(billy_bob)

print(immanuel.first_name)
print(immanuel.last_name)
print(immanuel.age)
print(immanuel.ceo.first_name)
# print(tom)
User.average_age()
User.check_age(nick, 21)
immanuel.birthday().greetings()