# import my_module
# importing my_module entirely will require you to call variables and functions
# by calling my_module.function() or my_module.var

# import as mm
# # allows you to normally shorten the name of the module like NumPy as np;
# # So that you can call any var, class or func in that module with mm.func()
# # mm.var, or obj = mm.Class(v1, v2)t my_modul

from my_module import find_index as fi, test as tst

# simply put it is two different styles with which you can import functions and variables;
# in this fashion with from module import function;
# and you can call it without the need to do modulename(or moudleas).funct or moudle.var;
# you can just call it as var, or funct (or whatever you saved it as)
# you can import specific functions or variables, again as something else.
# But everything else in the module will nto be available to you.

print(tst)
courses = ['history', 'math', 'physics', 'compsci']
index = fi(courses, 'math')
print(index)


# from my_module import *
# this imports everything, but.
# this is frowned upon as we don't know what came from that module and what didn't.



# When you import modules, python looks for modules in its given PATH directories;
# This includes your current working directory among many other paths.
# You can see your path variables by doing the following;
import sys
print(sys.path)
# If your module is NOT in the predefined path directories, you will not be able to import the module;
# And python will raise an error if you try to do so.
# So then you can add the path that the module is in to the environment PATH variable;
# As sys.path is really a list
# Or you can also just move the module into somewhere in the existing PATH variable.

# The first way that you can add to the path variable is by...
# sys.path.append('wherever the new path may be')
# this adds the new path to the sys.path variable.
# But this is not that desirable, so we can add it to the PATH environment variable instead of hardcoding this.

# mac / linux
# nano ~/.bash_profile
# export PYTHONPATH="directory"

# windows you can add the path that the module is in through your ENV variables.
# Computer -> properties -> advanced settings and add env variables.

# After python searches your current working dir, it searches the standard library directories;
# This is what allows us to import things from the stnadard library without installing other things.
# See standard_lib.py for practice;
