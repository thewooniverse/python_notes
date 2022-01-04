print('Enter the first number to add:')
first = input()

print('Enter the second number to add:')
second = input()

print('Enter the third number to add:')
third = input()

print('The sum is ' + first + second + third)




"""
While this program below doesn't crash.
The sum is obviously wrong as it prints a string and not the actual sum;
which is caused by the input being string.

Press Run -> Run Module
(with Debug -> Debugger enabled and all four checkboxes on teh Debug Control window enabled)


The program stats in a paused state on line 1.
The line will often be highlighted.
The debug control window will be highlighted to show you where the program execution currently is.

Click the Over button once to execute the first print() call.
User Over instead of Step because you don't want to step into the code for the print() function.
Then the debug window will update to line 2 and the next line is highlighted.
When you press Over on line 2, IDLE waits for you to type something for the input() call into the interactive shell.

Keep going and you'll see the Globals section get populated as you keep going.


Stepping through the program with the debugger is helpful but can also be slow.
Often times you'll want the program to run normally until it reaches a certain line of code.

You can configure the debugger to do this with breakpoints!
See coinFlip.py for this exercise.
"""



