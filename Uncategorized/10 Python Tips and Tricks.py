from getpass import getpass



### Tip 1 : ternary conditions / operators ###
## can save writing a lot of unnecessary code

condition = False

# if condition:
#     x = 1
# else:
#     x = 0

## this can entirely be rewritten by writing this
x = 1 if condition else 0
print(x)
## does the same thing but in a single line of code
## single line doesn't mean its better but we're always going for simplicity and readability.




### Tip 2: working with big numbers ###
num1 = 10_000_000_000
num2 = 100_000_000
total = num1 + num2
# print(total)
## increases readability and prevents mistakes with hard to read numbers
## replaces commas that you'd use in handwriting without affecting the program output
# print(f'{total:,}')
## you can use an f string to format it out.


### Tip 3: preventing bad practices in opening / closing with context managers ###
## context managers manages resources for you so you don't have to do it yourself
## bad practice:
# f = open('test.txt', 'r')
# file_contents = f.read()
# f.close()
#
# with open('test.txt', 'r') as f:
#     file_contents = f.read()
    ## you don't have to manually close this file

## this example is with files, but it is applicable to anytime you're opening and tearing down resources.
## separate video on context management
## point of this video is to train yourself to try to make yourself aware of when to use context managers.



### tip 4: enumerators ###
## when you need a counter while looping over something
## this can make my code a lot cleaner.

names = ['c', 'b', 'd', 'woo']
index = 0
# for name in names:
#     print(index, name)
#     index += 1
## this is how beginners might do things, it works but is not very clean.
#
# for index, name in enumerate(names, start=1):
#     print(index, name)






### tip 5: zip function ###
## looping over two lists at once
names = ['pp', 'ck', 'ww', 'bw']
heroes = ['spiderman', 'superman', 'deadpool', 'batman']
universes = ['marvel', 'DC', 'Marvel', 'DC']
#
# for index, name in enumerate(names):
#     hero = heroes[index]
#     print(f'{name} is actually the initial for {hero}')
## this is one way of doing it but it is not that clean

# for name, hero, universes in zip(names, heroes, universes):
#     print(f'{name} is actually the initial of {hero} in {universes}')
    ## you can actually zip more than one list in a single unpack
## zip will simply stop after the shortest list has ended in the zip function.
## right now it iterates through all because they are all of the same length.
## unpacking is what we're doing here at line 82.

##### separate video for itertools #####






### tip6 : unpacking ###
items = (1, 2)
# print(items)
## instead
a, b = (1, 2)
# print(a)
# print(b)
# print(a, b)
## if your IDE throws an error for not using b, you can use an underscore instead
a, _ = (1, 2)
## convention is that if you use an underscore, it means you won't use that variable anywhere else in the code.

## unpacking and lengths
# try:
#     a, b, c = (1, 2)
# except ValueError:
#     print("YO")
## throws up an ValueError
## same for below
# a, b, c = (1, 2, 3, 4, 5)
## also ValueError because there is too many values to unpack
## you can prevent this by doing this
a, b, *c, d = (1, 2, 3, 4, 5)
## this allows c to be all of the rest, 3, 4, 5.
## you could also do *_, same underscore
# print(a)
# print(b)
# print(c)
# print(d)
## d after *c will make d the last value and c everything from after b to before d as c.


### tip7: getting setting attributes to objects ###
class Person():
    pass

person = Person()
# person.first = "Wooyoung"
# person.last = "Joo"
# print(person.first)
# print(person.last)
## you can dynamically set object attributes like this (though you should do this on a class level)
## you can set an attribute as a value of a variable with the setattr() function
# last = "Joo"
# setattr(person, 'first', 'Wooyoung')
# print(person.first)
# setattr(person, 'last', last)
# print(person.last)


person_info = {'first': "Wooyoung", "last": "Joo"}
for key, value in person_info.items():
    setattr(person, key, value)
print(person.first)
print(person.last)

for key in person_info.keys():
    print(getattr(person, key))


### tip8: sensitive information using getpass() function ###

## wrong way to do this
# username = input('username: ')
# password = getpass('password: ')
# print('Logging In...')
## you can see in terminal it will not reveal the password.



### tip 9: -m ###
## python -m venv my_env
## -m, -m will search sys.path for the named module and execute its contents as the main module
## basically what it means, it will run that specific model specified after -m.
## everything after that is arguments for that module.

### tip 10: Help / Dir ###
import smtpd
# help(smtpd)
## really smart devs who seem to know a lot don't memorize everything, they just know where to find stuff quickly.
## and they know / understand how to use it. Some of that has to do with knowing how to look stuff up
## and knowing what is available.
print(dir(smtpd))
## you can get just the attributes and methods of a module or even an object with dir()
## this way you get less info than help, but it may be easier to read.
##
print(dir("YO"))
## you can even do something like this, straight onto an object
## you can then spec the help function like this
help("YO".strip)
help(help)







