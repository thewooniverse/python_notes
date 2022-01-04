#! /usr/bin/python

"""
In this chapter, you'll learn a few ools and techniques to identify what exactly is going wrong.
First you will look at logging and assertions, two features that can help you detect bugs early.
Second you will look at how to use the Debugger - a feature of IDEL that executes a program one instruction at a time.
"""


import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')


"""
################################################   Raising exceptions   ################################################

Python raises an exception whenever it tries to execute invalid code.
In Chapter 3, we learnt about using try and except statements so that your program can recover from anticpated exceptions.
But you can also raise your own exceptions in your code.

Raising an exception is a way of saying "Stop running the code in this function and move the program execution to the except statement"

Exceptions are raised with a raise statement.
In code, a raise statement consists of the following:
- The raise keyword
- A call to the Exception() function
- A string with helpful error messages passed to the Exception() function
"""

# print(10/0) # ZeroDivisionError: division by zero
# raise Exception('This is the error message.') #Exception: This is the error message.




"""
If there are no try and except statements covering the raise statement that raise the exception,
The program simply crashes and displays the exception error message as above.

Often its the code that calls the function, not the function itself, that knows how to handle an exception.
So you will commonly see a raise statement inside a function, and the try and except statments in the code calling the function.
"""

def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2) + symbol))
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err) + '\n')





"""
########################################   Getting the Traceback as a string   #########################################

When Python encounters an error, it produces a treasure trove of error information called traceback.
The traceback includes the error message, the line nubmer of the line that cause the error,
and the sequence of the function calls that led to the error.

This squence of calls is called the call stack
"""

def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

# spam()

"""
Traceback (most recent call last):
  File "/Users/Joo/Desktop/Development/Python/Reference/automate the boring stuff with Python/c10_debugging/notes.py", line 83, in <module>
    spam()
  File "/Users/Joo/Desktop/Development/Python/Reference/automate the boring stuff with Python/c10_debugging/notes.py", line 78, in spam
    bacon()
  File "/Users/Joo/Desktop/Development/Python/Reference/automate the boring stuff with Python/c10_debugging/notes.py", line 81, in bacon
    raise Exception('This is the error message.')
Exception: This is the error message.

From the traceback, you can see that the error happened in line 83 in calling spam()
This particular call to the bacon() came from line 78, in spam.
Which calls bacon, in line 81 where it raises the exception.

The traceback is displayed by Python whenever a raised exception goes unhandled.
But you can also obtain it as a sring by calling traceback.format_exc()
This function is useful if you want the infromation from an exception's traceback but also want an except statement to gracefully
handle the exception.
You'll need to import the traceback module before calling this function.

For example, instead of crashing your program right when an exception occurs, you can write the traceback in information
to a log file and keep your porgram running.
You can look at the log file later, when you're ready to debug your program.
"""

import traceback

try:
    raise Exception('This is the error message.')
except:
    error_file = open('./note_files/error_info.txt', 'w')
    error_file.write(traceback.format_exc())
    error_file.close()
    print('The traceback info was written to error_info.txt\n')





"""
########################################################################################################################
####################################################   Assertions   ####################################################
########################################################################################################################

An assertion is a sanity check to make sure your code isn't doing something obviously wrong.
These sanity checks are performed by assert statements.
If the sanity check fails, then an AssertionError exception is raised.
In code, an assert statement consists of the following;
- The assert keyword
- a condition (that is, an expression that evaluats to True or False)
- a comma
- a string to display when the condition is False

"""

pod_bay_door_status = 'open'
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open".'

# pod_bay_door_status = "I\'m sorry Dave. I'm afraid I can't do that."
assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open.'




"""
Traceback (most recent call last):
  File "/Users/Joo/Desktop/Development/Python/Reference/boring_stuff/c10_debugging/notes.py", line 143, in <module>
    assert pod_bay_door_status == 'open', 'The pod bay doors need to be "open.'
AssertionError: The pod bay doors need to be "open.
"""




"""
#################################   using an assertion in a traffic light simulation   #################################
"""


market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switch_lights(stoplight):

    for key in stoplight.keys():

        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'

        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'

        elif stoplight[key] == 'red':
            stoplight[key] = 'green'


    assert 'red' in stoplight.values(), 'Neither light is red!!' + str(stoplight)

# switch_lights(market_2nd)

"""
You may already see the problem with this code, but lets say you didn't and wrote thousands of lines afterwards w/o noticing it.
When you finally run the simulation, the programs don't crash but the virtual cars do.

Since you've already written the rest of the program, you have no idea where the bug could be.
Maybe it's in the simulation code, or the code simulating the virutal drivers.
It could take hours to trace back the bug to the correct source which is the switch_lights() functon.

But if while writing swich lights, we put in the assetion to check that at least one of the lights is always red.
The assertion would crash with this error message:


    Traceback (most recent call last):
      File "/Users/Joo/Desktop/Development/Python/Reference/boring_stuff/c10_debugging/notes.py", line 173, in <module>
        switch_lights(market_2nd)
      File "/Users/Joo/Desktop/Development/Python/Reference/boring_stuff/c10_debugging/notes.py", line 171, in switch_lights
        assert 'red' in stoplight.values(), 'Neither light is red!!' + str(stoplight)
    AssertionError: Neither light is red!!{'ns': 'yellow', 'ew': 'green'}

"""





"""
###############################################   disabling assertions   ###############################################

Assertions can be disabled by passing the -O option when running Python.
This is good for when you have finished writing and testing your program and don't want it to be slowed down by
performing sanity checks (although most of the time assert statements do not cause noticeable speed difference)
Assertions are for development, not the final product.
By the time you hand off your program to someone else o run, it should be free of bugs and not require the
sanity checks.
See appendix B for details about how to launch your programs with the -O option.

syntax;
    python -O filename.py

"""




"""
########################################################################################################################
#####################################################   Logging   ######################################################
########################################################################################################################

Refer to factorialLog.py
"""












"""
########################################################################################################################
#################################################   IDLE's Debugger   ##################################################
########################################################################################################################

The debugger is a feature of IDLE that allows you to execute your program one line at a time.

The debugger will run a single line of code and the nwait for you to tell it to continue.
By running your program "under the debugger", like this you can take as much as time as you want to examine
the values in the variables at any given point during the program's lifetime.

This is a valuable tool for tracking down bugs;
You can basically see all the variables, and how they change, what functions are called, line by lne through a code.




### HOW TO ###
To enable IDLE's debugger, click Debug -> Debugger in the interactive shell window.
(open the shell window if you haven't already)

This will bring up the Debug Control window.
When the Debug control window appears, select all four of the Stack, Local, Source, and Globals checkboxes so that the window
shows the full set of debug information.

While the Debug Control window is displayed, any time you run a program from the file editor, the debugger will pause execution
before the first instruction and display the following:

- The line of code that is about to be executed
- A list of all local variables and their values
- A list of all global variables and their values

You'll notice that in the list of global variables, there are several variables you haven't defined,
Such as;
__builtins__
__doc__
__file__
and so on...
These are variables Python automatically sets whenever it runs a program.
The meaning of these are outside the scope of the course and can be ignored (but look into it if curious)


The program will stay paused until you press one of the five buttons in the Debug Conrol window:
Go, Step, Over, Out or Quit.

    ## GO ##
    Clicking the Go button will cause the program to execute noramlly until it terminates or reaches a breakpoint
    (breakpoints are described later in this chapter)
    If you are done debugging the program and want it to continue normally, click the Go button.

    ## Step ##
    Clicking the step button will cause the debugger to execute the next line of code and then pause again.
    The debug control window's list of global and local variables will be updated if their values change.
    If the next line of code is a function call - the debugger will "step into" that function and jump
    to the first line of code of that function

    ## Over ##
    Clicking the Over button will execute the next line of code, similar to the Step button.
    However, if the next line of code is a function call, the Over button will "step over" the code in
    the function. The function's code will be executed at full speed, and the debugger will pause as soon as
    the function call returns.

        For example, if the next line of code is a print() call, you don't really care about code inside the
        built-in print() function; you just want the string you passed it printed to the screen.

        For this reason, using the Over button is more common than the Step button.

    ## Out ##
    Clicking the Out button will cause the debugger to execute lines of code at full speed until it returns
    from the current function. If you have "stepped into" a function call with the Step button and now
    simply want to keep executing instructions until you get back out, click the Out button to "Step out"
    of the current function call.

    ## Quit ##
    If you want to stop debugging entirely and not bother to continue executing the rest of the program,
    click the Quit button.
    The Quit button will immediately terminate the program.
    If you want to run your program noramlly again, select Debug -> Debuger again to disable the debugger.





### Debugging a Number adding program ###
See buggy_adding_program.py in the cwd :)


### breakpoints ###
See coinFlip.py for this section!!



########################################################################################################################
#####################################################   summary   ######################################################
########################################################################################################################

Assertions, exceptions, logging and the debugger are all valuable tools to find and prevent bugs in your program.

Assertions with Python assert statements are a good way to implement "saniy checks" that give you an early warning
when a necessary condition doesn't hold true.
Assertions are only for errors that the program shouldn't try to recover from and should fail fast.
Otherwise, you should raise and exception.

An exception can be caught and handled by the try and except statements.

The logging module is a good way o look into your code while it's running and is much more convenient to use than the
print() function because of its different logging levels and ability to log to a text file.

The debugger lets you step through your program one line at a time.
Alterantively, you can run your program at normal speed and have the debugger pause exception whenever it reaches a line
with a breakpoint set.
Using the debugger, you can see the state of any variable's value at any point during the program's lifetime.

These debugging tools will help you write programs that work.
Accidentally introducing bugs into your code is a fact of life, no matter how many years of coding experience you have.


"""
