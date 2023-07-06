import random

class Character:
    
    def __init__(self, name, strength=10, speed=3, health=100):
        self.name = name 
        self.strength = strength
        self.speed = speed
        self.health = health
        self.moves = []
    
    def show_stats(self):
        all_attributes = self.__dict__
        for key in all_attributes:
            print(f"{key}: {all_attributes[key]}")
        return self
    
    #TODO modify_health
    def modify_health(self, amount):
        self.health += amount
        return self
    
    #TODO attack
    def attack(self, target):
        damage_amount = random.randint(0, self.strength)
        move_used = self.get_move()
        final_damage = damage_amount + move_used.damage_modifier
        #check to see if target dodges
        successful_dodge = target .dodge()
        # if not successful_dodge:
        if successful_dodge == False:
            print(f"{self.name} did {damage_amount} damage with a modifier of {move_used.damage_modifier} because he used {move_used.name} equaling a total of {final_damage}")
            target.modify_health(-damage_amount)
        return self
    
    def get_move(self):
        for idx, move in enumerate(self.moves):
            print(f"{idx+1}:{move}")
        move_idx = input("What move do you want?\n>>>")
        if not move_idx.isdigit():
            print("sorry that is an incorrect option, try again")
            self.get_move()
        else:
            return self.moves[int(move_idx)-1]
            
    #TODO dodge
    def dodge(self):
        # get a random number between 0 and 20
        # if the number falls in their speed allowance then successful dodge
        dodge_num = random.randint(0, 20)
        print(f"{self.name} rolled a {dodge_num} and needed something below a {self.speed}")
        if dodge_num > self.speed:
            #unsuccessfully dodge the attack
            print(f"{self.name} got hit")
            return False
        else:
            print(f"{self.name} dodge the attack")
            return True
    
    def add_move(self, move):
        self.moves.append(move)