from classes.character import Character

class Orc(Character):
    def __init__(self, name, strength=13, speed=1, health=110):
        super().__init__(name, strength, speed, health)