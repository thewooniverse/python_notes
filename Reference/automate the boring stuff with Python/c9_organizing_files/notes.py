#! usr/bin/env python3




"""
########################################################################################################################
################################################   The shutil module   #################################################
########################################################################################################################

Shell Utilities (shutil) module has functions to let you copy, move, rename, and delte files in your python programs
"""

import shutil, os, sys
# import send2trash
import zipfile

try:
    os.makedirs(os.getcwd() + '/test_files')
except:
    pass


"""
############################################   copying files and folders   #############################################

The shutil module providees functions for copying files, as well as entire folders.

shutil.copy(source, destination) will copy the file at the path source to the folder at the path destination.
(both source and destinations are strings)
If the destination is a filename, it will be used as the new name of the copied file.
This function returns a string of the path of the copied file.
"""

os.chdir('./test_files') # changes to test filese
shutil.copy('test.txt', '../kinda_testyyy.md') #filepath with basename passed as second param, this name is used but content copied.
# works with .md as well
shutil.copy('test.txt', './one_more_level') # directory passed as second param, same name is used


"""
While shutil.copy() will copy a single file, shutil.copytree() will copy an entire folder and every folder and file contained in it.
Calling shutil.copytree(source, destination) will copy the folder at the path source, along with all its files and subfolders,
To the folder at path destination.
Both parameters are string formats.
The funcion creates this and returns the string path of the copied folder;

The function call also creates a new folder.
"""
try:
    shutil.copytree('./one_more_level', './one_more_backup')
except:
    print('{0} filepath already exists'.format('one_more_backup'))



"""
######################################   Moving and Renaming Files and Folders   #######################################

Calling shutil.move(source, desination) will move the FILE OR FOLDER at the path source to the path destination.
and will return a string of the absolute path of the new location

If destination points to a folder, the source file gets moved into destination and keeps its current filename.
If a file exists in the destination folder with the same name, it would be over written (its easy to make this mistake)
The destination can also specify a filename, if it does - the same overwrite logic applies, or it is renamed.

THe folders that make up the destination must already exist, otherwise Python will throw an exception.
"""

shutil.move('../kinda_testyyy.md', './testes.txt')
# moved kinda test that was created in the previous exercise to current working directory which is test_files and renamed it testes.

shutil.move('./testes.txt', './doesnt_exist')
# The destination doesnt_exist, doesn't exist - and therefore the .md file is turned into a directory






"""
######################################   permanently deleting files and folders   ######################################

- os.unlink(path) will delete the file at path
- os.rmdir(path) will delete the folder at path. THis folder must be empty of files or folders.
- shutil.rmtree(path) will remove folder at path, and all the files and folders it containts will also be deleted.

ALL of these permanently deletes and it is irreversible.
So it's often a good idea to print() calls to show the files that are deleted while the delete call is commented out.
Because if you make a typo, say you wrote .xt instead of .txt - you would remove every file with .xt extension unintentionally.
"""

for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)






"""
#####################################   safe deletes with the send2trash module   ######################################

A much better way to delete files is with the third party send2trash module.
You can install this by installing send2trash from a terminal window if its not already installed.
This delete is reversible because send2trahs send the files deleted to your computer's trash or recycle bin instead of
permanently deleting them.
"""

bacon_file = open('bacon.txt', 'a')
bacon_file.write('bacon not a veggie')
bacon_file.close()
# send2trash.send2trash('bacon.txt')
# creates then deletes.






"""
#############################################   Walking a directory tree   #############################################

Say you want to rename evry file in some folder, and every file in evey sub folder of that folder.
That is you want to walk through the directory tree, touching each file as you go.
Writing a program like this could be tricky, however Python provides a funcion to handle this process for you.

THe os.walk() function is passed a single string value: the path of a folder.
You can use os.walk() in a for loop to walk a directory, much like the range() function to walk over a range of numbers.
However, unlike range() the os.walk() function will return three values on each iteration throug hthe loop:

1. A string of current folder's name
2. A list of strings of the folders in the current folder
3. A list of strings of the files in the current folder

By current folders, it is meant the folder for the current iteration of the for loop.
The current working directory is NOT chagned by the os.walk() function.
"""

for folderName, subfolders, filenames in os.walk(os.path.abspath('.')):
    print('the current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER of' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ": " + filename)

print('\n\n\n')


# for folder_name, sub_folders, filenames in os.walk('/.'):
#     print(folder_name)
#     print(sub_folders)
#     print(filenames)










"""
####################################   compressing files with the zipfile module   #####################################

ZIP files can hold compressed contents of many other files.
Compressing a file reduces its size, which is useful when transferring it over the Internet.
Since a ZIP file can also contain multiple files and subfolders, it's a handy way to package several files into one.
This single file, called an archive file, can then be, say, attached to an email.

Your python programs can both create and open ZIP files using the zipfile module.
"""


"""
### Reading zip files ###

To read the contents of a zip file, first you must create a ZipFile object
ZipFile objects are conceptually similar to the file objects we saw returned by the open() function in the previous chapter.
They are values through which the program interacts with the file.

zipfile.ZipFile() function creates an object.
Passing it with a .zip file's filename.
Note that zipfile is the name of the python module,, and ZipFile() is the name of the function.
"""

# moving example.zip to current working directory
# shutil.move('../../course_materials/example.zip', '.') # successfully moved to current working directory test_files.

"""
A zipfile object has a namelist() method that returns a list of strings for all the files and folders contained in the ZIP file.
These strings can be passed to get the getinfo() zip file method to return a ZipInfo objec about that particular file.
ZipInfo objects have their own attributes such as;
- file_size in bytes
- compress_size in bytes

"""
print(os.getcwd())
example_zip = zipfile.ZipFile('example.zip')
print(example_zip.namelist())

spam_info = example_zip.getinfo('spam.txt')
print('Compressed file is {0}x smaller!!'.format(round((spam_info.file_size / spam_info.compress_size), 2)))
example_zip.close()





"""
### Extracting from Zip Files ###

The extractall() method for ZipFile objects extracts all the files and folders from a ZIP file into the current workign dir.
You can also pass a foldername to extractall() to have it extract the files into a folder other than the curren workign dir.
If the folder passed to exractall() does not exist, it will be created.

The extract() method for ZipFile objects will extract a single file from the ZIP file.
The string you pass to extract() must match one of the srings in the list returned by namelist().
Optionally, you can pass a second argument to extract() to extract file into a different folder other than the cwd.
If the second argument is a folder that doesn't yet exist - it will create the folder.
"""

example_zip = zipfile.ZipFile('example.zip')
example_zip.extractall('./example_folder/')
example_zip.extract('spam.txt', './spam_folder')
example_zip.close()



"""
### Creating and adding to ZIP files ###

To create your own compressed ZIP files, you must open the ZipFile object in write mode by passing 'w' as second argument.
(This is similar to opening a text file in write mode by passing 'w' to the open() function)

When you pass a path to the write() method of a ZipFile object, python will compress the file at that path and addit to the ZIP file.
The write() method's fist agument is a string of the filename to add.
The second argument is the compression type parameter, which tells the computer what algorithm it should use to compress the files.
You can just set this value to zipfile.ZIP_DEFLATED (This specifies the deflate compression algorithm which works well with most data types.)

Keep in mind that when you open a file in 'w write mode' - it will erase all existing contents of a ZIP file.
If you want to simply add files to an existing ZIP file, pass 'a' as the second argument instead of 'w' to open it in append mode.
"""

new_zip = zipfile.ZipFile('new.zip', 'w')
new_zip.write('bacon.txt', compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()
# this creates a new ZIP file named new.zip with bacon.txt inside it.





















"""
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------   personal notes   --------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

Basically, all of the stuff I can do with shell script - like rm, mv, rename, cp etc...
Can all be done in Python scripts as well.
It's just really different ways to talk to the computer, and Python as my first language is often the preferred way to do it.


Also notetaking like this is quite helpful, these are basically distilled cheatsheets I can always revert back to.
Continuously tweak, test out and play with.
"""


