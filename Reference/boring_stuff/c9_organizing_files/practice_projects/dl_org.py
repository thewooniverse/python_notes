#! usr/bin/python
# dl_org.py - download organizer, locates the downloads folder in a system on which it is run and organizes it.
# currently, it moves all PDF into a single folder, all doc and docx into a single folder, svg / png into a folder, jpeg into a folder
# As well as mp3 into a separate folder.

import re, os, shutil, sys
from pathlib import Path

# get the home directory then the Downloads directory
home = str(Path.home())
downloads_dir = os.path.join(home, 'Downloads')
print(downloads_dir)

# define the folders and the file extension types I want in them in a dictionary
filetype_dict = {"Music": ['mp3'], "PDF": ['pdf'],
"Vector Images": ['svg', 'png'], "Documents": ['doc', 'docx'],
"Installaters": ['exe', 'dmg']}


# create the relevant directories within it if it doesn't exist already;
for key in filetype_dict.keys():
    try:
        os.makedirs(downloads_dir + f'/{key}')
    except:
        pass


# compile a dictionary of foldername and regex.
regex_dict = {}
for key, value in filetype_dict.items():
    regex_obj = re.compile(r'.({0})$'.format('|'.join(item for item in value)))
    print(regex_obj)
    regex_dict[key] = regex_obj



# listdir to get all the filenames / basenames of files in here, excluding directories.
filenames = os.listdir(downloads_dir)


# iterate through the filename
for filename in filenames:
    for foldername, regex in regex_dict.items():
        mo = regex.findall(filename)
        if mo: # if there is a match at all.
            shutil.move((downloads_dir + os.path.sep + filename), (downloads_dir + os.path.sep + foldername))









# move each file depending on regex match to the relevant folder.


