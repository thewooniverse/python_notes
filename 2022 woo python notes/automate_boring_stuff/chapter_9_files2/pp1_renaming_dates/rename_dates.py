#! python
"""
rename_dates.py - script to rename american dates to european dates 
(or any other dates for that matter)
"""
import shutil
import os
import re

cwd = os.getcwd()

# Create regex to identify american dates
amdate_regex = re.compile(r"""
((0|1)?\d)-      # 0, or 1 starting, month. 1-2 digits
((0|1|2|3)?\d)-  # 0,1,2,3 starting, day, 1-2 digits
(\d{1,4})       # 1-4 digits for the year
(.*?)$          # all test after the date
""", re.VERBOSE)


# os walk to get all the relevant filenames and regex through them
# while walking, when matched, rename into correct format with matched object
# rename the file with shutil.move (no need to waste memory to delete and recreate)
for foldername, subfolders, filename in os.walk(os.getcwd()):
    for file in filename:
        if amdate_regex.search(file):
            abs_wd = os.path.abspath('.') + os.path.sep + 'test_dates'
            # print(abs_wd)
            mo = amdate_regex.search(file)
            MM, DD, YY = mo.group(1), mo.group(3), mo.group(5)
            ext = mo.group(6).strip()
            US_date = f"{'-'.join([MM,DD,YY])}{ext}"
            EU_date = f"{'-'.join([DD,MM,YY])}{ext}"

            # abs working directory for each of the files
            US_wd = abs_wd + os.path.sep + US_date
            EU_wd = abs_wd + os.path.sep + EU_date
            with open(US_wd, 'w') as changed_date:
                changed_date.write("changed Foobar")

            # move to rename
            shutil.move(US_wd, EU_wd)
