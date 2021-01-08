

"""
########################################################################################################################
#############################################   Introduction and basics   ##############################################
########################################################################################################################
"""

import os
# print(os.getcwd())

"""
###########################################   basic files and directories   ############################################

A file has two key properties: a filename (usually written in one word) and a path.
The path specifies the location of a file on he compuer.
Every program that runs on your computer has a current working directory or cwd.



#############################   backslash on windows and forward slash on osx and linus   ##############################

On Windows paths are written using \ backslashes as the separator between folder names.
On OS X and Linux, the forward slash / is used as the separator.

Each operating system also has a different home / root directory.
For OSX it's /.
For Windows it's C:\

Windows and OS X are both not case sensitive;
Linux is the only OS whose directory names are case sensitive.


Commands like:
os.path.join() and os.getcwd() return different results depending on the OS that we are running on, and can be
quite useful in writing programs that can run smoothly on any OS.

######################################   os.path.join() os.getcwd() os.chdir()   #######################################
"""

test_dir = os.path.join('usr', 'bin', 'spam')
# print(test_dir) # in macOS prints usr/bin/spam
# print(test_dir) # on windows this returns usr\\bin\\spam -- becaus you need to escape each backslash by another backslash.

#  os.path.join() is helpful when you need to create strings for filenames.
my_files = ['accounts.txt', 'details.csv', 'docs.txt']
# for filename in my_files:
#     print(os.path.join('usr/bin/spam/eggs', filename))

# os.getcwd()
cwd = os.getcwd()
# print(cwd) # /Users/Joo/Desktop/Development/Python/Reference/automate the boring stuff with Python/c8_readwrite_files

# os.chdir()
# os.chdir('/Users/Joo/Desktop')
# print(os.getcwd()) # now prints /Users/Joo/Desktop


"""
#####################################   creating new folders with os.makedirs()   ######################################

Your programs can create new directories with this command.
It will create any necessary intermediate folders in order to ensure that the full path exists.
"""

import os
# os.makedirs('./NOW/NOWNOW') # this has created folders on the Desktop because I changed the dir to desktop.









"""
###########################################   Absolute vs. Relative paths   ############################################

There are two ways to specify a file path.
- An absolute path, which always begins with the root folder
- A relative path, which is relative tot he program's current working directory

There are also . and .. folders, which I am familiar with.
The single period . for a foldername is shorthand for this directory
Two periods .. means the parent folder.


######################   os.path.abspath(path) os.path.isabs(path) os.path.relpath(path, start)   ######################

- Calling os.path.abspath(path) will return a string of the absolute path of the argument.
- This is an easy way to convert a relative path into an absolute one.

- Calling os.path.isabs(path) will return True if the argument is an abso- lute path and False if it is a relative path.

- Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path.
- If start is not provided, the current working directory is used as the start path.
"""

# os.chdir('/Users/Joo/Desktop/Development/Python/Reference')
# print(os.getcwd())

# print(os.path.abspath('.')) #/Users/Joo/Desktop/Development/Python/Reference/automate the boring stuff with Python/c8_readwrite_files
# print(os.path.abspath('../../')) # /Users/Joo/Desktop/Development/Python/Reference
# print(os.path.isabs('.')) # False
# print(os.path.isabs('/Users/Joo/Desktop/Development/Python/Reference')) # True
# print(os.path.isabs(os.path.abspath('.'))) #True

# print(os.path.relpath('Users/Joo/Desktop', 'Users/')) # Joo/Desktop
# print(os.path.relpath(os.getcwd(), '/Users/')) # make sure to put the / at the start of Users.
# prints Joo/Desktop/Development/Python/Reference/automate the boring stuff with Python/c8_readwrite_files



## both of these commands print the same director
# print(os.path.abspath('.'))
# print(os.getcwd())





"""
###########################################   dirname(path) basename(path)   ###########################################

GETTING DIFFERENT PARTS OF THE FILEPATH
- Calling os.path.dirname(path) will return a string of everything that comes before the last slash in the path argument.
- Calling os.path.basename(path) will return a string of everything that comes after the last slash in the path argu- ment.
"""
notes_filepath = os.getcwd() + '/notes.py'

# print(notes_filepath) #/Users/Joo/Desktop/Development/Python/Reference/automate the boring stuff with Python/c8_readwrite_files/notes.py
# print(os.path.basename(notes_filepath)) # notes.py
# print(os.path.dirname(notes_filepath)) # /Users/Joo/Desktop/Development/Python/Reference/automate the boring stuff with Python/c8_readwrite_files


## os.path.split(filepath) is a handy shortcut if you need both values of dirname and basename to a filepath
# print(os.path.split(notes_filepath)) # returns a tuple
# ('/Users/Joo/Desktop/Development/Python/Reference/automate the boring stuff with Python/c8_readwrite_files', 'notes.py')

## if you want to get a list of string for each folder (for use in os.path.join() in other OS)
# print(notes_filepath.split(os.path.sep)) # call the split() stringm ethod to return a list of each part of the path.
# ['', 'Users', 'Joo', 'Desktop', 'Development', 'Python', 'Reference', 'automate the boring stuff with Python', 'c8_readwrite_files', 'notes.py']

# print(os.path.sep) # / -- this is your separator for your os

rejoined_path = os.path.sep.join(notes_filepath.split(os.path.sep))
# /Users/Joo/Desktop/Development/Python/Reference/automate the boring stuff with Python/c8_readwrite_files/notes.py
# print(rejoined_path)




"""
######################################   Finding file sizes and folder contents   ######################################

Now that you have ways of handling filepaths, you can start gathering information about specific files and folders.

- Calling os.path.getsize(path) will return the size in bytes of the file in the path argument.
- Calling os.listdir(path) will return a list of filename strings for each file in the path argument.
- (Note that this function is in the os module, not os.path.)
"""
# print(os.listdir(os.getcwd())) #['notes.py', 'test.md']
# print(os.path.getsize(os.getcwd() + '/notes.py')) #7646

# total_size = 0
# for filename in os.listdir(os.getcwd()):
#     total_size += os.path.getsize(os.path.join(os.getcwd(), filename))
# print(total_size) # 7791






"""
##############################################   checking path validity   ##############################################

Many python functions will crash with an error if you supply them with a path that does not exist.
os.path module offers functions to check whether a path exists or not.

- os.path.exists(path) will return True if file or folder referred to in the argument exists and False if otherwise.
- os.path.isfile(path) will return True if the path argument exists and is a file and False if else.
- os.path.isdir(path) will return True if path argument exists and is a directory and False if else.
"""
# print(os.path.exists('/Users/')) # True
# print(os.path.isfile('/Users')) # False
# print(os.path.isfile(os.getcwd() + '/notes.py')) # True
# print(os.path.isdir('/Users')) # True

































"""
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------   personal notes   --------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
"""
