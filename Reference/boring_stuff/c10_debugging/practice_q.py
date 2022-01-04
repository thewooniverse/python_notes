


#1
assert spam < 10 and type(spam) == int(), "Spam must be an integer less than 10"

#2
assert eggs.lower() == bacon.lower(), "The string must be the same, not case sensitive"

#3
assert '' == None, "Always asserting"



"""
#4
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

#5
import logging
logging.basicConfig(filename='mylog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

#6
Debug, Info, Warning, Error, Critical

#7
logging.disable(logging.CRITICAL)
At the start of the program

#8
- you don't accidentally delete prints intended for end user
- you can easily turn on and off different levels of logging and disable it

#9
Step - goes to next line / executes and steps INTO functions
Over - goes to next line, and if it is a function, steps over function and just executes
Out - similar to running "go" inside a local function the code has stepped into, it will run until the given function stpped into is finished
and pause at next stop

#10
It will stop either when it finishes, or runs into a breakpoint, or an error.

#11
A breakpoint is a defined line of code in IDLE editor, where when running Go in debugger - it will stop at that line and pause.

#12
You right click on a line you want to stop in the file editor.



"""
