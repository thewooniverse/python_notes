print('Imported my module :)')
# Note that when we import an entire module, everything in that is run.
# That's why we wouldn't really have test functions like print this or that in the module that we want to import.
# Rather it would be better to have variables, classes and functions defined.
# Though for practice sake, this was put in.

import os
import sys
# remember you can import other modules within your modules;
# in order to write more complex modules.



test = "Test String"

def find_index(to_search, target_val):
    '''Find the index of a value in a given sequence'''
    for i, value in enumerate(to_search):
        if value == target_val:
            return i

    return False




