class Character:
    
    def __init__(self, name):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self
    
    def attack(self, target):
        target.health -= self.strength
        return self
    
    def show_health(self):
        return self.health