from classes.elf import Elf
from classes.human import Human
from classes.orcs import Orc
from classes.game import Game

owen = Elf("Owen")
tyler = Human("Tyler")

owen.attack(tyler)

tyler.show_stats()

owen.show_stats()
g1 = Game(owen,tyler)
g1.battle()