

"""
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
---------------------------------------------   SECTION 1 PYTHON BASICS   ----------------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
"""


"""
//////////////////////   falsey and truthy stuff review   /////////////////////
"""


ls = ['', None, False, 0, []]
# for i in ls:
#     if not i:
#         print(('its not ' + str(i)), end="  ")


# mutable, immutable objects
# pointing to the same object / reference
# same value;
# is means the same object
# == evaluates the value.

lis1 = ['a', 'b', 'c']
lis2 = lis1
lis3 = lis1[:]  # same function as lis1.copy()

# if lis1 == lis2:
#     print("lis1 == lis2")

# if lis1 is lis2:
#     print("lis1 is lis2")

# if lis3 is lis1:
#     print("lis1 is lis3")  # not printed, because they are not

# if lis3 == lis1:
#     print("lis3 == lis1")


### practice project for lists ###

# comma code
spam = ['apples', 'bananas', 'tofu', 'cats']
cheese = ", ".join(item for item in spam)
# print(cheese)

# character picture grid
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for y in list(range(len(grid) - 1)):
    string = ""
    try:
        for row in grid:
            string += row[y]
    except IndexError:
        # print("\nyou've reached the end!")
        break
    # print(string)


### practice project for dictionaries ###
import pprint

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    print("Inventory: ")
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
    print("Total number of items: " + str(sum(inventory.values())) + "\n")


# display_inventory(stuff)


def add_to_inventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1


add_to_inventory(stuff, dragonLoot)

# display_inventory(stuff)


print(len("https://www.w3schools.com/python/ref_func_print.asp#:~:text=The%20print()%20function%20prints,before%20written%20to%20the%20screen.)"))


### working with strings ###
# print("say hi to Bob\"s mother!\\")
# print(r'that\scarrolscat')
# raw strings simply consider backslashes as part of the string and not as the start of an escape character.

# print('''Dear Alice, \n
# Eve's cat has been arrested for catnapping, cat burglary, and extortion.
# Sincerely, \n
# Bob''')


print('Hello'.rjust(100, "#"))
print('Hello'.ljust(100, "#"))
print(' Hello '.center(100, "#"))


### practice project for strings ###


"""
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
--------------------------------------   SECTION 2 - Automate the boring stuff   ---------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
"""


### practice questions for regex ###

### practice project for regex ###
