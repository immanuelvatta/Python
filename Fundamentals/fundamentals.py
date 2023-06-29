# this is a comment!
"""
this is a multi line comment !!!
"""

#variables
#primitive

#no declarator
# snake case
#no semicolons
my_name = "Immanuel"
my_number = 13
my_float = 3.14

#booleans need to be capitalized
is_admin = True

print("Hello World " + str(my_number))

#JS console.log(`this is a var ${varName}`)

print (f"hello {my_number}")

#composite

#in JavaScript we have arrays

#in Python we have lists

my_nums = [11,22,33,44,55]

print(my_nums)
print(my_nums[0])
#remove the last element from a list
my_nums.pop()
print(my_nums)

#add an element to the end
# JS array.push()
# python list.append()

my_nums.append(my_name)
print(my_nums)

#get the length of this list

print(len(my_nums))


# JS Objects
# Python Dictionary

# key-value pairs
# they are comma separated
# all keys are 'strings'


first_pokemon = {
    'name' : 'Arbok',
    'power' : 9001,
    'is_pokemon' : True,
    'hobbies' : [
        '⛷️', '🍴', '😎']
}

#print 'Arbok'
print(first_pokemon['name'])


print(first_pokemon['hobbies'])
#show the first hobby  of the dict.
print(first_pokemon['hobbies'][0])


#functions
#a set of instructions

def greeting(some_name):
    if(some_name == 'Immanuel'):
        print("Welcome back")
    elif(some_name == 'bob'):
        print("hello bob!")
    else:
        print("hello " + some_name)
    return 33

print(greeting("bob"))

# how do i loop in Python?
# for _iterator_ in _ collection_:

# range() - returns a sequence of numbers
# range(start, stop, end)
# start - inclusive optional - default is 0
# stop - exclusive REQUIRED
# step - optional, increment(-/+)

# 1 - 10
for i in range(1,11,1):
    print(i)


# print all elements in a list ( without an index)
for element in my_nums:
    print(element)


for i in range(len(my_nums)):
    print (my_nums[i])