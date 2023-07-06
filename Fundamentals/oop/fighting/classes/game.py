import random

class Game:
    
    def __init__(self, c1,c2):
        self.c1 = c1
        self.c2 = c2
        self.turn = c1 if random.randint(0,100)%2 ==0 else c2
        self.not_turn = c1 if random.randint(0,100)%2 ==0 else c2
        
    def battle(self):
        while self.c1.health>0 and self.c2.health >0:
            self.end_turn()
            
    def end_turn(self):
        self.c1.show_stats()
        self.c2.show_stats()
        if self.turn == self.c1:
            self.turn = self.c2
            self.not_turn = self.c1
        else:
            self.turn = self.c1
            self.not_turn = self.c2
            
    def end_game(self):
        if self.c1.health > 0:
            print(f"Player{self.c1.name} is the winner!!!!")
        else:
            print(f"Player{self.c2.name} is the winner!!!!")