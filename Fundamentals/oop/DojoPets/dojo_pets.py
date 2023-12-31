class Ninja:
    
    #TODO implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name , treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # implement the following methods:
    #TODO walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self

    #TODO feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):

        if len(self.pet_food) > 0:
            #decrement food list
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Oh no!!! you need more pet food!")
        return self

    #TODO bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()

class Pet:

    #TODO implement __init__( name , type , tricks ):
    def __init__(self, name , type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 25
        self.noise = noise

    # implement the following methods:
    #TODO sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self

    #TODO eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    #TODO play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    #TODO noise() - prints out the pet's sound
    def noise(self):
        print(self.noise)





treats = ['Sausage','Bacon',"Fruits"]
pet_food = ['Pizza','Burger']

my_pet = Pet("Mr. Nibbles","Dog",['run','jump','sit','fetch'],"bork bork")

immanuel = Ninja("Immanuel","V",treats,pet_food, my_pet)

immanuel.feed();
immanuel.feed();
immanuel.feed();