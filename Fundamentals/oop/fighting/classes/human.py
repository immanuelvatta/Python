from classes.character import Character
from classes.move import Move
class Human(Character):
    def __init__(self, name, strength=10, speed=5, health=102):
        super().__init__(name, strength, speed, health)
        
        self.add_move (Move("Human Spirit", 20))
        self.add_move  (Move("Swift Blade", 50))
        self.add_move  (Move("Shield Slam", 0.5))
        
        