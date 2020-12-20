### 1: IndentationError ###

nums = [11, 30, 44, 54]

for num in nums:
    square = num ** 2
    print(square)


## this is more commonly a problem that you encounter using simple text editors
## IDEs like PyCharm usually solves this problem


### 2: ImportError ###
## say you have a new module named math.py in your current working directory
## if within that file, you try to say from math import radians
## you won't be able to import radians and will get an ImportError because it will try to import from our own math
## module, instead of the standard library because it takes priority over searching in the standard library.
## to fix it, you just need to rename math.py, to something like project_module.py

## ImportErrors are usually problems with either your sys.path or filename clashes like this

## this can happen on the script / program level as well when we try to name a variable the same thing as
## something that we are importing.
## because there is nothing that prevents us from preventing using a variable name that is a part of a module

## a large part of learning to code is learning how to understand errors like these and learn to solve them
## understanding how to read error messages to learn to solve where the problem may be.


### 3: mutable default args ###
def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)






emps = ['John', 'Jane']
add_employee('corey')
add_employee('joo')


## this keeps adding every time the function is called.
## this is because default arguments are evaluated once at the time of the function creation

def add_employee2(emp, emp_list=None):
    if not emp_list:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)


add_employee2('corey')
add_employee2('joo')
## now this works as intended.

import time
from datetime import datetime


def display_time(time=None):
    if time is None:
        time = datetime.now()
    print(time.strftime('%B %d, %Y %H: %M:%S'))


display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()
## we may have expected seconds to increase, but it hasn't for the same reason as above.
## we evaluate the default value once at the time of function creation.

## this is likely an error, well not really an error, it works but it doesn't produce the results I expect.






### 4: Iterators and exhaustion ###
## in python 3.0 if we zip() we are returned with a zip object and not a printed list.
## still we can throw it in a list() function again to change it back to a list of tuples of zipped list.

names = ['pp', 'ck', 'ww', 'bw']
heroes = ['spiderman', 'superman', 'deadpool', 'batman']
universes = ['marvel', 'DC', 'Marvel', 'DC']

identities = zip(names, heroes)
print(list(identities))

for identity in identities:
    print(f'{identity[0]} is actually {identity[1]}')
## the above two lines code doesn't iterate through the zip object because it is exhausted.
## zip is an iterator - iterators can be exhausted.
## that means we can iterate through and access their value one time, but we can't do it again.
## and we exhausted it in print(list(identities))

## instead what we could do is...
identities = list(zip(names, heroes))
print(identities)
for identity in identities:
    print(f'{identity[0]} is actually {identity[1]}')

## lists are not exhausted, iterators ARE exhausted.
## it all boils down to performance and efficiency.




### 5: importing bad practices ###
## using asterisk in import - which imports everything in a given module
## as you can recall you can do import os to import whole modules
## but then you need to call things like os.rename()
## rather you can do from os import rename, remove - to just be able to use rename()
## if you do from os import * -> allows us to rename() remove() without using os.
## but this is bad practice;
## this makes your code hard to debug and introduce new errors
## like when you import * from two modules and they clash like they both have escape function.

## so just import explicitly, and use as XYZ, to avoid clashes when importing two functions of the same name
## like
## from html import escape as esc
## from glob import escape as escape
## or alternatively you can just import html, and import glob - and just do html.escape()







