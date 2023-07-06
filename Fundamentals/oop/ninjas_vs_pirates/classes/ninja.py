from classes.character import Character
#! Ninja -> child | Character -> parent (inheritance)
class Ninja(Character):

    def __init__( self , name ):
        super().__init__(name)
        self.name = name
        self.strength = 12
        self.speed = 5
        self.health = 100
    # def show_stats( self ):
    #     print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
    # def attack( self , target ):
    #     target.health -= self.strength
    #     return self
