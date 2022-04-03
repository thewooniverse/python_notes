#! python3
"""
typo_corrector.py - a script that runs through a directory and finds / fixes a bunch of
typos (dependent on what typos we are looking for). Mostly puncutation typos will be
detected in the first version.

"  " - double spaces
'. s' - uncapitalized word after a period requireds
"""
# compile both regex types
import re
import logging
import os
logging.basicConfig(level=logging.DEBUG, filename=f'{os.getcwd()+os.path.sep}error_logs/typo_corrector.txt',
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug(f'\nstart of program---!')


# regex definitions
test = '  abcd  . aaab. Aaab'

doublespace_regex = re.compile(r"""(\s\s)""", re.VERBOSE)
dotspace_lower_regex = re.compile(r"([.]\s[a-z])")
logging.debug(doublespace_regex.findall(test))
logging.debug(dotspace_lower_regex.findall(test))


def upper_repl(match):
    """
    Helper function for returning the uppercase first chracter of each word detected.
    """
    return match.group(1).upper()


logging.debug(dotspace_lower_regex.sub(upper_repl, test))


def replace_typos(text):
    """
    executes all types of typo corrections based on preconstructed regex patterns
    """
    text = doublespace_regex.sub(' ', text)
    text = dotspace_lower_regex.sub(upper_repl, text)
    return text


test_file_Adir = os.getcwd() + os.path.sep + 'test_files'
test_files = os.listdir(test_file_Adir)

for file in test_files:
    test_file = test_file_Adir+os.path.sep+file
    txt = ""
    with open(test_file) as rf:
        txt = rf.read()
        logging.debug(txt)

    with open(test_file, 'w') as wf:
        txt = replace_typos(txt)
        txt = replace_typos(txt)
        wf.write(txt)
        logging.debug(txt)
