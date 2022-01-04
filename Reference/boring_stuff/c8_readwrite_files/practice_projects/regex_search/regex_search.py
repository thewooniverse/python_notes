#! /usr/bin/python
# regex_search.py, a script that searches all files in a folder and searches for any lines that matches a user-supplied regular expression.
# results are printed onto the screen, and placed in a .result.txt file in the passed folder;
# the folder passed to the function should be in absolute format.


import os, sys, shutil, re



# print(tst_path)

# extract the path and other important sys argv
path = r'{0}'.format(sys.argv[1])
os.chdir(path)
# TODO: catch error for relative path.
if not os.path.isabs(path):
    # raise

# compile the regex
eth_addr_regex = re.compile(r'0x[a-f0-9]{40}', re.I)

# listdir to get a list of files in the directory
file_list = os.listdir(path)

# open the write file, if it exists, search num two
with open('.results.txt', 'w') as wf:

    # iterate through each file in the directory file_list
    for file in file_list:

        # if the file is not .results.txt
        if file != '.results.txt':

            # open the file as rf
            with open(file, 'r') as rf:
                wf.write('\n\nSearching {0} for pattern...:\n\n'.format(file))

                # read lines
                lines = rf.readlines()

                # for each line, regex search
                for line in lines:
                    mo = eth_addr_regex.findall(line)

                    # if mo exists, lists are truth when there are elements
                    if mo:
                        # add each match in mo to writefile.
                        for match in mo:
                            wf.write(match + '\n')
                        wf.write('\n')








