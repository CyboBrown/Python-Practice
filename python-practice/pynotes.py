# single-line comment
"""
multiline comment (or undeclared string)
"""

# ### INPUT AND OUTPUT
# name = input("Name: ") # asks input with prompt and stores it to var "name"
# print("Hello,", name) # prints and concatenates string with automatic spaces
# number = float(18) # converts int to float, typecasting
# print("Hello, " + "I am %s, %d years old." % (name, int(number))) # concatenates string (no space), uses placeholders

# ### LISTS
# mylist = [] # creates list
# mylist.append(1) # push()
# mylist.append(2)
# mylist.append(3)
# print(mylist[2]) # prints at index 2 of list
# for x in mylist: # prints entire list
#     print(x)
# points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
# print(points.count(9)) # counts the number of elements with the specified value

# ### OPERATORS
# print(10 % 3) # prints remainder
# print(2 ** 3) # prints exponent result
# print("Hel" + "lo!") # concatenates string
# hellos = "hello" * 10 # repeats string
# print(hellos)
# even_numbers = [2,4,6,8]
# odd_numbers = [1,3,5,7]
# all_numbers = odd_numbers + even_numbers # combines list
# print(all_numbers)
# print([1,2,3] * 3) # repeats list
# name = "John"
# if 4 in even_numbers: #  checks if a specified object exists within an iterable object container, such as a list
#     print("4 is even.")
# x = [1,2,3]
# y = [1,2,3]
# print(x == y) # Prints out True
# print(x is y) # Prints out False # "is" does not match the values of the variables, but the instances themselves
# print(not False) # Inverts

# ### STRINGS
# astring = "Hello world!"
# print(astring.index("o")) # returns the index of the first instance of "o" in the string
# print(astring.count("l")) # counts the instance of "l" in the string
# print(astring[3:7]) # prints from index 3 to index 7 (without including 7)
# print(astring[3:7:1]) # [start:stop:step]
# print(astring[3:7:2])
# print(astring[::-1]) # reverses string
# print(astring.upper()) # capitalize string
# print(astring.lower())
# print(astring.startswith("Hello"))
# print(astring.endswith("asdfasdfasdf"))
# afewwords = astring.split(" ") # splits string at space
# print(afewwords[0])
# print(afewwords[1])

# ### LOOPS
# primes = [2, 3, 5, 7]
# for prime in primes:
#     print(prime)
# # May also use xrange()
# for x in range(5): # Prints out the numbers 0,1,2,3,4
#     print(x)
# for x in range(3, 6): # Prints out 3,4,5
#     print(x)
# for x in range(3, 8, 2): # Prints out 3,5,7
#     print(x)
# # Python also utilize while loops and break/continue features
# # You may also use "else" for loops

# ### FUNCTIONS
# def my_function(username, greeting):
#     print("Hello, %s , From My Function!, I wish you %s."%(username, greeting))
# def sum(a, b):
#     return a + b
# my_function("CyboBrown", "good health") # functions can only be called after defining it
# print(sum(10, 15))

# ### CLASSES AND OBJECTS
# class Vehicle: # define the Vehicle class
#     name = ""
#     kind = "car"
#     color = ""
#     value = 100.00
#     def description(self):
#         desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
#         return desc_str
# car1 = Vehicle()
# car1.name = "Ferrari"
# car1.color = "yellow"
# car2 = Vehicle()
# car2.name = "Ranger"
# car2.color = "blue"
# print(car1.description())
# print(car2.description())
# class NumberHolder:
#    def __init__(self, number):
#        self.number = number
#    def returnNumber(self):
#        return self.number
# var = NumberHolder(7)
# print(var.returnNumber())

# ### DICTIONARIES
# phonebook = {}
# phonebook["John"] = 938477566
# phonebook["Jack"] = 938377264
# phonebook["Jill"] = 947662781
# # You can also do it this way:
# """
# phonebook = {
#     "John" : 938477566,
#     "Jack" : 938377264,
#     "Jill" : 947662781
# }
# """
# print(phonebook)
# del phonebook["John"] # deletes a dictionary entry
# # phonebook.pop("John") <- alternative way of deleting
# for name, number in phonebook.items(): # iterating over dictionaries
#     print("Phone number of %s is %d" % (name, number))

# ### MODULES AND PACKAGES
# # import random             // imports the random module
# # from random import randint // imports randint object from random module
# # import random.randint
# # from random import *      // import all objects from random module
# # import randint as random_integer   // imports randint object with custom import name
# # PYTHONPATH=/foo python game.py
# # // specify additional directories to look for modules
# # // enables the script to load modules from the foo directory, as well as the local directory
# # You may also use the sys.path.append function. Execute it before running the import command:
# # sys.path.append("/foo")
# # # import the library
# # import urllib
# # # use it
# # urllib.urlopen(...)
# import random
# # dir(random)
# help(random)
