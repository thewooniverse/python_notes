#! python3
"""
file_searcher.py - a script that searches a directory (or directorie(s) of abspath) for emails

"""
import re
import os
import logging

# logging config
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('start of program!')


# create regex object for email
emailRegex = re.compile(r"""(
    [a-zA-Z0-9.%+-]+  # username, 1 or more
    @                 # @ symbol
    [a-zA-Z0-9.-]+    # domain name
    (\.[a-zA-Z]{2,4}) # dot something
    )
    """, re.VERBOSE | re.IGNORECASE
                        )

# search each file in test_files for correct email syntax / regex
f = open(f"{os.getcwd()+os.path.sep}results.txt", 'w')

test_abspath = os.getcwd() + os.path.sep + "test_files"
files = os.listdir(test_abspath)
count = 0
for file in files:
    file_path = test_abspath+os.path.sep+file
    assert os.path.isabs(file_path)
    with open(file_path) as cfile:
        content = cfile.read()
        logging.debug(content)
        logging.debug(emailRegex.search(content))

        if emailRegex.search(content):
            f.write(f'{content} found in {str(file)}\n')
            count += 1
f.write(f"\n\nTotal matches is: {count}!")

# for each file found

# also export error logs
