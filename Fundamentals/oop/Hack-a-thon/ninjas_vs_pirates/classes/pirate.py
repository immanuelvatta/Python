from classes.character import Character
class Pirate(Character):

    def __init__(self, name):
        super().__init__(name)
        self.name = name 
        self.strength = 20
        self.speed = 2
        self.health = 150




    # def show_stats( self ):
    #     print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    # def attack ( self , target ):
    #     target.health -= self.strength
    #     return self

