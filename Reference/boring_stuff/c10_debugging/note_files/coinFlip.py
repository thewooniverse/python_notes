import random
heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads += 1

    if i == 500:
        print('Half way done!!')

print('Heads came up ' +str(heads) + ' times.')




"""
If you ran this program under the debugger, you would have to click the
Over button thousands of times before the program terminated.
If you were interested in teh value of heads and the halfway point of the program's
execution, when 500 of 1000 flips were completed,
you could instead just set a breakpoint on the line print('Halfway done!')

To set a breakpoint,
right click the line in the flie editor and select Set Breakpoint.

You don't want the breakpoint on the IF statement, because the if statement
is executed through every single iteration of the loop.

The line with the breakpoint will be highlighted in yellow in the file editor.
When you run the program under the debugger, it will start in a paused state
at the first line, as usual.

But if you click Go, the program will run at full speed until it reaches the line
with the breakpoint set on it.
You can then click Go, OVer, Step or Out to continue as normal.


If you want to remove a breakpoint, right click on the line in the file editor
and select clear breakpoint from the menu.
The yellow highlighting will disappear and the debugger will not break
on that line in the future.

"""
