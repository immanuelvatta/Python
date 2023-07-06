
class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    
    def __init__( self, first_name, last_name, pet, treats, pet_food):
        pass
    #! implement the following methods:
    #TODO walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        pass
    #TODO feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        pass
    #TODO bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        pass
    
class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        pass
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        pass
    # play() - increases the pet's health by 5
    def play(self):
        pass
    # noise() - prints out the pet's sound
    def noise(self):
        pass