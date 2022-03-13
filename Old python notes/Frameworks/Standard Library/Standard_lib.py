# Standard Lib is written by some of the best coders
# Good practice to use the tried and true standard lib;
# You could probably write some of these yourself, but these are well optimized and written.
# Below are some good standard libraries to practice;


# Random module
import random
courses = ['math', 'math hl', 'biz', 'cs', 'physics']
print(random.choice(courses))





# math
import math
rads = math.radians(90)
print(math.sin(rads))


# datetime and calender
import calendar
import datetime

today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

# os module
import os
print(os.__file__)
# prints C:\Users\joowo\anaconda3\lib\os.py
# these are python files, in the library.
# you can go in and play with different .py files in the standard library.

# import antigravity
# This is a joke / comic that is delivered with the standard library.
# When you run it, it imports other modules and opens up a browser with a comic.




# non standard - watchdog

