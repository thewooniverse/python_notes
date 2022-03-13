
# Variable scope
# Understanding how scope works is important in working with language
# As well as in debugging code when diff variables return values we didn't expect.

# Variable scope determines where our variables can be accessed from.
# and what values those variables hold in different contexts.

# LEGB
# Local, Enclosing, Global, Built-in
# Local - variables defined in a function
# Enclosing - variables in the local scope in a enclosing functions
# Global - variables defined at the top level of a module, or explicitly declared global using the global keyword.
# Built-ins - preassigned variable names that are preassigned in python.

# This is the order that determines what variables are assigned to;
# Python first checks the variables in the local scope
# then the enclosing scope, then global then built ins.


######
######

# global and local

# x = 'global x'
# this is a global variable, because it is in the main body of a file.

def test():
    y = 'local y'
    x = 'local x'
    print(y)
    print(x)

test()
# prints local y and local x
# print(y)
# doesn't work, error is raised because the y variable doesn't live outside the local function.
# print(x)
# prints global x, because local x doesn't live outside of test function.

def test2():
    # global x
    # though it is gone over here, it is never really used that much in coding
    x = "local x"
    print(x)

test2()
# prints local x
# It actually doesn't need the global x to be defined in line 24;

# using the local scopes of a function makes things easier to work with
# using global function too often will lead to a lot of hard coding and trouble in bug shooting.
# as the local scope is contained we don't have to worry about what happens outside the function.


def test3(z):
    print(z)

test3('local z')
# This is another example of local;




######
######

# Built in
m = min([5, 4, 3, 2, 1, 0, -5])
print(m)
# builtin function that finds the smallest value of an iterable
# again use the dir() method to see all the available builtins
import builtins
print(dir(builtins))

# you CAN rewrite / overwrite a builtin function and its functionality;



######
######

# Enclosing

def outer():
    x = 'outer x'
    # local to our outer function

    def inner():
        # nonlocal x
        # this works like global keyword, but with the enclosing function.
        # nonlocal unlike global is actually useful
        # because it can change things like states and decorators within functions

        x = 'inner x'
        # local to our inner function
        # if this is commented out...
        # calling outer() will print 'outer x' twice.
        # This is what the enclosing scope means
        # When we call x in the inner();
        # it prints 'inner x'
        # but if x is not defined in inner()
        # then, it looks for the next best thing which is the enclosing function (local)
        # enclosing local.
        print(x)



    inner()
    print(x)
    # if x is not defined in either of these areas, then it will simply all on global x;

outer()

# local to that inner functions
# local to its enclosing functions
# global to the document
# builtins to language

