from classes.character import Character
from classes.pirate import Pirate
from classes.ninja import Ninja

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")
char3 = Character("Test")
# char3 = ("Test Character")
# char3.show_stats()

#develop character
#loop 2 opponent till one dies (could turn it into a class)
#ninja class that inherits from character (modify ninja class)
#pirate class 


# michelangelo.attack(jack_sparrow)
# jack_sparrow.attack(jack_sparrow)
# michelangelo.attack(jack_sparrow)
#! if statement end of each turn check health character.show_health
#! if character.show_health <= 0, other character win
# jack_sparrow.show_stats()
# michelangelo.show_stats()



'''#TODO 
while char1.show_health() > 0 and char2.show_health > 0:
    if char1.show_health <= 0
        print char 2 wins
    elif char2.show_health <= 0
        print char 1 wins
    else
        turn = 1
        if turn ==1
        if char1's turn
            #char1's turn
            turn= 2
        if turn == 2
            #char2's turn
            turn = 1
            continue
'''

def arena(char1, char2):
    while char1.show_health() > 0 and char2.show_health() > 0:
            turn = 1
            if turn == 1:
                print(f"{char1.name}'s turn ")
                char1.attack(char2)
                print(f"{char2.name}'s health: {char1.show_health()}")
                        
                turn = 2
            if turn ==2:
                print(f"{char2.name}'s turn ")
                char2.attack(char1)
                print(f"{char1.name}'s health: {char1.show_health()}")
                turn = 1
                continue

    if char1.show_health() <= 0:
            return (f"{char2.name} won")
    if char2.show_health() <= 0:
            return (f"{char1.name} won")

print(arena(michelangelo, jack_sparrow))