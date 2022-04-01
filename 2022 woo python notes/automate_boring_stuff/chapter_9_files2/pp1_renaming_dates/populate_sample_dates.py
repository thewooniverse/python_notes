#! python3
"""
A small script to prepare myself for the practice project (since there were
no downloadable files)

"""

import os
import random

# create random dates
date_range = (list(range(1, 2030)), list(range(1, 12)), list(range(1, 31)))
cwd = os.getcwd()

# for each, create a file in test_dates
for i in list(range(100)):
    day, month, year = random.choice(date_range[2]), random.choice(
        date_range[1]), random.choice(date_range[0])

    with open(f".{os.path.sep}test_dates{os.path.sep}{month}-{day}-{year}.txt", 'w') as test_date:
        test_date.write("foobar")

# clean the folder test_dates for any incorrect files;
# (IF I want to, I want to.)
m31 = [1, 3, 5, 7, 8, 10, 12]
m30 = [4, 6, 9, 11]
for filename in os.listdir(cwd+os.path.sep+"test_dates"):
    os.chdir(cwd+os.path.sep+"test_dates")
    M, D, YE = filename.split('-')
    if (int(D) == 31) and (int(M) not in m31):
        print("This is not a valid 31 day month!")
    elif (int(D) == 30) and (int(M) not in (m31 + m30)):
        print(f"{D,M,YE}This is not a valid 30 day month!")
        os.unlink(f'{filename}')
