num1 = 42 #- variable declaration int
num2 = 2.3 # - variable declaration float
boolean = True # - variable declaration boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # - variable declaration lists
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # - variable declaration dictionaries 
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration tuples
print(type(fruit)) #output : <class 'tuple'>
print(pizza_toppings[1]) # output: Sausage
pizza_toppings.append('Mushrooms') # adding mushrooms to the end of pizza_toppings
print(person['name']) #output: John
person['name'] = 'George' #updates the existing key called name, so John gets updated to George
person['eye_color'] = 'blue' # adds eye_color key-value pair and assigns blue as its value
print(fruit[2]) # output: banana

if num1 > 45: # conditional check to see if num1= 42 is  greater than 45
    print("It's greater") # output : It's greater if num > 45 (which its not: wont get logged)
else: # checks if if num1 < 45 
    print("It's lower") #output : It's lower

if len(string) < 5: # conditional check to see if string length is less than 5
    print("It's a short word!") # output: It's a short word! (if string length is less than 5)(which its not: wont get logged)
elif len(string) > 15: # conditional to check if string length is greater than 15
    print("It's a long word!") # output: It's a long word! (if string length is greater than 15) (which its not: wont get logged)
else: #checks if its greater than 5 but less than 15
    print("Just right!")# output: Just right!

for x in range(5): #essentially translates to for x in range(0,5,1)
    print(x) # output: 0,1,2,3,4
for x in range(2,5): #essentially translates to for x in range(2,5,1)
    print(x) # output: 2,3,4
for x in range(2,10,3):
    print(x) # output: 2,5,8
x = 0
while(x < 5): # same as for x in range(5): print x
    print(x) # output: 0,1,2,3,4
    x += 1

pizza_toppings.pop() #removes the last element:  Mushrooms
pizza_toppings.pop(1) #removes the element at index 1: Sausage

print(person) # output {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': 'blue'}
person.pop('eye_color') # removes the specified key from person
print(person) #output {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
    """ output:
        After 1st if statement
        After 1st if statement
        After 1st if statement
    """
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()
""" output:
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
"""
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
"""output:
    Hello
    Hello
    Hello
    Hello
"""

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
"""output:
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
"""
print_hello_x_or_ten_times(4)
"""output:
    Hello
    Hello
    Hello
    Hello
"""

"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)