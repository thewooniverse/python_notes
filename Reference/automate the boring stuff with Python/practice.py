
# falsey and truthy stuff review

ls = ['', None, False, 0, []]
for i in ls:
    if not i:
        pass
        # print(('its not ' + str(i)), end="  ")


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


### practice project for strings ###


### practice questions for regex ###

### practice project for regex ###
