#! usr/bin/python


"""
########################################################################################################################
#####################################################   Logging   ######################################################
########################################################################################################################

If you ever put a print() statment in your code to output some variable's value while your program is running,
you've used a form of logging to debug your code.
Logging is a great way to understand what's happening in your program and in what order it is happening.

Python's logging module makes it easy to create a record of custom messages that you write.
These log messages will describe when the program execution has reached the logging function call and list any variables
you have specified at that point in time.

On the other hand, a missing log message indicates a part of the code was skipped and never executed.



Logging is built for developers, and it is a much handier / cleaner / less error prone way of seeing whats happening
Instead of using print() function everywhere.

#############################################   using the logging module   #############################################

To enable the logging module to display log messages on your screen as your program runs,
copy the following ot the top of your program (but under the #! shebang line)

    import logging
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

You don't need to worry too much about how it all works, but basically, when Python logs an evnt, it creates a
LogRecord object that holds information about that event.
The logging module's basicConfig() function lets you specify what details about the LogRecord object you want
to see and how you want those details displayed.

Say you wrote a function to calculate the factorial of a nubmer (refer to factorialLog.py)
"""

"""
Say you wrote a function to calculate the factorial of a number. In math- ematics, factorial 4 is 1 × 2 × 3 × 4, or 24.
Factorial 7 is 1 × 2 × 3 × 4 × 5 × 6 × 7, or 5,040. Open a new file editor window and enter the following code.
It has a bug in it, but you will also enter several log messages to help yourself figure out what is going wrong.
"""
import logging

logging.basicConfig(filename='program_log.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
# changing level=logging.ERROR and to different levels, DEBUGs and other messages are ignored

logging.debug('Start of program\n')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))

logging.debug('End of program')

# help(logging.debug)



"""
Here we use the logging.debug() function when we want to print log information.
This debug () function will call basicConfig(), and a line of information will be printed.
This information will be in the format we specified in basicConfig() and will include the messages we passed to debug().
The print(factorial(5)) which is (0) call is part of the original program,
so the result is displayed even if logging messages are disabled.

Output looks something like this.

     2021-01-10 18:51:42,512 -  DEBUG -  Start of program
     2021-01-10 18:51:42,512 -  DEBUG -  Start of factorial(5%)
     2021-01-10 18:51:42,512 -  DEBUG -  i is 0, total is 0
     2021-01-10 18:51:42,512 -  DEBUG -  i is 1, total is 0
     2021-01-10 18:51:42,512 -  DEBUG -  i is 2, total is 0
     2021-01-10 18:51:42,513 -  DEBUG -  i is 3, total is 0
     2021-01-10 18:51:42,513 -  DEBUG -  i is 4, total is 0
     2021-01-10 18:51:42,513 -  DEBUG -  i is 5, total is 0
     2021-01-10 18:51:42,513 -  DEBUG -  End of factorial(5%)
    0
     2021-01-10 18:51:42,513 -  DEBUG -  End of program


Immediately we can see that the total is 0 during the entire loop, which immediately points out what is going on and where.
Which allows us to fix the program easily.


Logging messages provide a trail of breadcrumbs that can help you figure out when things started to go wrong like this.



#############################################   don't debug with print()   #############################################
Typing import logging and
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
is somewhat unwieldy.

You may want to use print() calls insteadbut don't give into this temptation.
Once you're done deubgging, you'll end up spending a lot of time removing print() alls from your code for each log message.

You might even accidentally remove some print() calls that were being used for nonlog messages.

The nice thing about log mesages is that you're free to fill your program with as many as you like,
and you can always disable them ater by adding a single logging.disable(logging.CRITICAL) call.

Unlike print() the logging module makes it easy to switch between showing and hiding log messages.


Log messages are intended for the programmer, not the user.
The user won't care about the contents of some dictionary value you need to see to help with debugging;
use a log message for something like that.
For messages that the users will want to see, like File not found, Invalid inpu, please enter a number you can use a print() call.








##################################################   logging levels   ##################################################
Logging levels provide a way to categorize your log messages by importance.
(so that you can logging.disable(logging.LEVEL) varying levels of debug messages).
There are five logging levels, described in the table Logging Levels in the same folder / directory.
Messages can be logged at each level usign a different logging function like..

DEBUG - logging.debug() - lowest level. used for small details. Usually you care about these messages in diagnosing problems.
INFO - logging.info() - used to record information on general events in your program or confirm that things are workign at their point in the program.
WARNING - logging.warning() - used to indicate a potential probelm that doesn't prevent the progam from working but might do so in teh future.
ERROR - logging.error() - Used to record an error that caused the program to fail to do something.
CRITICAL - logging.critical() - The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop entirely.

Your logging message is passed as a string to these functions.
The logging levels are suggestions.
ultimately it is up to you to decide which category your log messages falls into.

The benefit of logging levels is that you can change what priority of logging messages you want to see.
Passing logging.DEBUG to the basicConfig() function's level keyword will show messages from all the logging levels.
But afer developign your program more, you may bei nterested only in errors.

In that case, yu can set basicConfig()'s level argument tologging.ERROR. This will only show EROR and CRITICAL messages.
And skip the DEBUG, INFO, and WARNING messages.
(achieving similar results to logging.disable(logging.LEVEL))

"""
# logging.disable(logging.CRITICAL) # having this disables all the logging messages below.
print('\n\n')

logging.debug('some debugging details.')
logging.info('The logging module is working')
logging.warning('An error message is about to be logged...')
logging.error('An error has occured.')
logging.critical('The program is unable to recover!!')












"""
################################################   disabling logging   #################################################

After you've debugged your program, you don't want all these messages cluttering your screen.

As you've already seen with logging.disable(logging.LEVEL) and basicConfig's level=logging.LEVEL... you can disable some or most messages.
The logging.disable() function disables these so that you don't have to go into your program to remove all the logging calls by hand.

YOu simply pass logging.disble() a logging level and it will suppress all log messages at that level or lower.
So if you want to disble logging entirely, you just add logging.disable(logging.CRITICAL) to your program.

#### logging.disable() will only disable the relevant levels of logging messages that come after it.
So you'll probably want to add it near the import logging line of the code in your program.
"""




"""
################################################   logging to a file   #################################################

Instead of displayng the log messages ot the screen, you can also write them to a text file.
The logging.basicConfig() function takes a filename keyword argument like so:


    import logging
    logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - $(levelname)s - %(message)s')


The log messages will be saved to myProgramLog.txt.
While logging messages are helpful ,they can clutter your screen and make it hard to read the program's output.

Writing the logging messages to a file will keep your screen clear and store the messages so you can read them after running the program.
You can open this plaintext file in any text editor -- textedit or notepad.

Note that the error log appends files / folders that are already existing.
And creates the file if it does not exist yet.
"""




