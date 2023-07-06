from classes.character import Character
from classes.move import Move
class Elf(Character):
    def __init__(self, name, strength=9, speed=10, health=105):
        super().__init__(name, strength, speed, health)
        self.add_move(Move("Nature's Fury", 10))
        self.add_move(Move("Shadow Dance", 20))
        self.add_move(Move("Arcane Eruption", 50))