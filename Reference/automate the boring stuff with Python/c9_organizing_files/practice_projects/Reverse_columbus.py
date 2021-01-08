#! /usr/bin/python
# Reverse_columbus.py - a script that reverts american style dates to european style dates in a defined directory

"""
## Reuqirements
- Searches all the filenames in the given directory for American-style dates
- When one is found, it renames the file with the month and day swapped to make it European-style
- MM-DD-YYYY is American DD-MM-YYYY is European


## V2 requirements
- Allow for reverse, default = False.
"""


# import modules
import os, re, shutil


# create a regex object that identifies the pattern of dates.
date_regex = re.compile(r"""
    (
    ^(.*?) # any text that comes before
    ((0|1)\d) # month 2 digits
    ([-./:]) # separator
    ((0|1|2|3)\d) # day, 2 digits
    ([-./:]) #separator
    ((19|20|21)\d\d) #YYYY
    (.*?)$ #all text that comes afer
    )
    """, re.VERBOSE)

# call os.listdir() on defined directory to get a list of the files.
filenames = os.listdir('./date_files/')
print(filenames)


# loop over each filename, using regex to check whether it has a date
for filename in filenames:
    result = date_regex.search(filename)
    if result:
        text_before, mm, dd, yyyy, text_after = result.group(2, 3, 6, 9, 11)

        abs_path = os.path.abspath('./date_files')
        amer_filename = os.path.join(abs_path, filename)
        euro_filename = os.path.join(abs_path, text_before + dd + '-' + mm + '-' + yyyy + text_after)
        # print(abs_path)
        shutil.move(amer_filename, euro_filename)


