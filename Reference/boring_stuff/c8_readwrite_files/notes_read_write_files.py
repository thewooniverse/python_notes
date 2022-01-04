#! usr/bin/env python3

import os
import shelve
import pprint


"""
########################################################################################################################
#########################################   The file reading/writing process   #########################################
########################################################################################################################

Now that you are comfortable working with folders and paths (rel, abs), you'll be able to specify the location of files
To read and write.

##### Plaintext files #####
The functions covered in the next few sections will apply to platinext files;
Plaintext files contain only basic text characters and do not include font, size or color information.
The text files with the .txt extension or Python script files with .py extensions are examples of plaintext files
These can be opened with Notepad or TextEdit applications.
Your programs can easily read the contents of plaintext files and treat them as an ordinary stirng value.

Binary files on the other hand are all other filetypes, such as .doc, .pdf, images, .xml, .exe, .dmg
If you open a binary file in Notepad or TextEdit it will look like scrambled nonsense.

Since every different type of binary file must be handled in its own way, we won't go into too much depth reading and writing
binary files directly. However there are many modules present in Python that make working with binary files of different
format easier - you will explore some of them, like the shelve module later.
"""

# make sure the directory we are working with is correct
print(os.getcwd())
os.chdir(os.getcwd() + '/test_files/')
print(os.getcwd())



"""
#######################   basic workflow in working with files - open() read() write() close()   #######################

The three steps to reading / writing files in Python;
1. Call the open() function to return a file object
2. Call the read() or write() method on the file object.
3. Close the files by calling the close() method on the file object

We're working with file objects here.



1. Opening files with then open() function
The open() function returns a File object.
A file object represens a file on your computer, it is simply another type of value in Python.
Much like lists and dictionaries you're already familiar with.
After saving a returned file object from a open() function call, you can now call methods on the File object.
"""
hello_file = open(os.getcwd() + '/test.txt')
# print(hello_file)
# <open file '/Users/Joo/Desktop/.../test.txt', mode 'r' at 0x10a731390>
# default mode is r, read mode - where you are only able to read data from teh file, not write or modify in any way.
# you can also write this default as an argument explicitly, by writing 'r' as the second argument t open()

# print(hello_file.name) # filepath
# print(hello_file.mode) # r



"""
2. Reading the contents of Files
Now that you have a file object, you can start reading form it.
You can use the File object's read() and other methods.

2.a. read()
If you think that the contents of a file as a single large string, the read() method returns the string that is storedi n that file.

2.b. readlines()
Alternatively, you can use the readlines() method to get a list of string values from the file.
One string for each line of text.
reads ALL lines in a list format

2.c. readline()
Reads the next line

Once the file is open, and read - it stays there.
So if you do readlines, and a readline - you'll get nothing because you'll already be at the end of the line.
"""

# hello_content = hello_file.read()
# print(hello_content)
hello_lines = hello_file.readlines()
# print(hello_lines)
hello_file.close()
#['This file is a test file, for reading I must say!!\n', '\n', '\n', 'And later now, we have a sonnet\n', 'The sonnet is a popular classical form that has compelled poets for centuries.
# Traditionally, the sonnet is a fourteen-line poem written in iambic pentameter, employing one of several rhyme schemes, and adhering to a tightly structured thematic organization.\n']



"""
3. Writing and appending to files to files
Python allows you to write content to a file in a similar way to how the print() function writes to the screen.
YOu can't write a file once you've opened it in read mode.
So you can instead open it in write mode.


If the filename passed to open does not exist, both write mode and append mode will create a new blank file.
After reading or writing a file, call the close()


3.a. write mode
Write mode will overwrite the existing file and start from scratch, just ike when you overwrite a variable's value with a new value.
You can open a File object in write mode by passing 'w' as the second argument

Note that write mode does not automatically add a new line, and that you'll have to do this yourself.


3.b. append mode
Append mode on the other hand will append the text to the end of the existing file.
You can think of this as appending to a list in a variable, rather than overwriting the variable altogether.
Pass 'a' as the second agument to open() to open the file in append mode.


"""
bacon_file = open(os.getcwd() + '/bacon.txt', 'w')
bacon_file.write('Hi world!\n')
bacon_file.write('test!!')
bacon_file.close()
# this creates a bacon.txt (if it doesn't exist) in the current working directory, and writes Hello world! to it.

bacon_file = open(os.getcwd() + '/bacon.txt', 'a')
bacon_file.write('Bacon is not a vegetable.\n')
bacon_file.close()

bacon_file = open(os.getcwd() + '/bacon.txt')
bacontent = bacon_file.read()
bacon_file.close()
# print(bacontent)
# Hi world!
# Bacon is not a vegetable.






"""
################################################   tell() and seek()   #################################################

# f.tell() shows you the position that we are currently read into
# f.seek() allows us to point where we are in a file to a specific location
"""

with open('test.txt', 'r') as rf:
    print(rf.tell()) # 0
    size_to_read = 3
    rf_content = rf.read(size_to_read)
    wf = open('test2.txt', 'w')
    wf.write(rf_content)
    print(rf.tell()) # 3
    rf.seek(0)
    size_to_read_2 = 6
    rf_content = rf.read(size_to_read_2)
    wf.write(rf_content)
    wf.close()
    wf = open('test2.txt', 'r')
    wf_content = wf.read()
    print(wf_content)
    wf.close()













"""
########################################################################################################################
#################################################   context managers   #################################################
########################################################################################################################

context managers allows us to work with the file within the block and it automatically closes the files.
so it is considered best practice to use them
we can still access after the variable f like with
print(f.closed)
but you are not able to read the file because it is closed and it will throw an error.
"""


# print(os.getcwd())

with open('bacon_number_5.txt', 'w') as wf:
    wf.write('hi')

with open(os.getcwd() + '/bacon_number_5.txt', 'r') as rf:
    with open('bacon_number_5_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)







"""
#####################################   saving variables with the shelve module   ######################################

You can save variables in your python program to binary shelf files using the shelve module.
This way your progam can restore data to variables from teh hard drive.
The shelve module will let you add Save and Open features to your program.

Plaintext is useful for creating files that you'll read in a text editor such as Notepad or TextEdit.
But if you want to save data from your Python programs, use the shelve module.

For example, if you ran a program and entered some configuration settings, you could save those settings to a shelf file
and then have the program load them the next time it is run.

Your programs can use the shelve module to later reopen and retrieve the data from these shelf files.
Shelf values don't have to be opened in read or write modethey can do both once opened.
"""

### reading and writing data using shelve module
shelf_file = shelve.open(os.getcwd() + '/mydata')
# shelve.open() and pass it a filename, and then store the returned shelf value in a variable.
cats = ['McGonagall', 'Snoopy', 'Chimi', ' Churri']
shelf_file['cats'] = cats
# you can make changes to your shelf value as if it were a dictionary.
shelf_file.close()


"""
running this file you will see new files in the current working directory.
on windows mydata.bak, mydata.dat and mydata.dir - on OS X a single mydata.db file will be created.
these binary files conain the data you stored in your shelf.
The format of these binary files are not important, you only need to know what the shelve module does,
now how it does it. The module frees you from worrying about how to store your program's data to a file.
"""


shelf_file = shelve.open(os.getcwd() + '/mydata')
type(shelf_file)
# print(shelf_file['cats'])
shelf_file.close()


"""
Just like dictionaries, shelf values have keys() and values() methods that will return list-like
values of the keys and values of the shelf.
Since these methods return list-like values instead of true-lists, you should pass them int oa list()
function to get them in true list form.
"""

shelf_file = shelve.open(os.getcwd() + '/mydata')
key_list = list(shelf_file.keys())
# print(key_list)
value_list = list(shelf_file.values())
# print(value_list)
items_list = shelf_file.items()
# print(items_list)
shelf_file.close()





"""
###############################   saving variables with the pprint.pformat() function   ################################

pprint.pprint() 'pretty prints' THE CONTENTS of a list or dictionary's values to the screen.
pprint.pformat() does the same thing but instead of printing it to screen, it returns it as a string.

Not only is this string formatted to be easy to read, but it is also syntactically correct Python code.

Say you have a dictionary stored in a variable, and you want o save this variable and its contents for future use.
Using pprint.pformat() will give you a string that you can write to a .py file.
This file will be your very own module that you can then import whenever you want to use the variable stored in it.
"""

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}] # a list of dictionaries
# print(pprint.pformat(cats))
# print(os.getcwd())
file_obj = open('../myCats.py', 'w')
file_obj.write('cats = ' + pprint.pformat(cats) + '\n')
file_obj.close()

"""
Here, to keep the list in cats available even after we close the shell, we use pprint.pformat() to return it as a string.
Once we have the data in cats as a string, its easy to write the string to a file, which we'll call myCatspy
"""

import myCats
# # # only works if it is in PATH or in the cwd
# print(myCats.cats) # [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# print(myCats.cats[0]) # {'name': 'Zophie', 'desc': 'chubby'}
# print(myCats.cats[0]['name']) # Zophie


"""
### The modules that an import statements imports are themselves just Python scripts. ###

So when the string from the previous section are saved to a .py file in the correct syntax -
it is a module that can be imported just like any other.
And since Python scripts are themselves just text files with the .py file extension, your python programs can even generate
other Python programs, you can hen import these files into scripts.

The benefit of creating a .py file (as opposed to saving variables in the shelve module) is that because it is a text file,
The contents of the file can be read and modified by anyone with a simple txt editor.
For most applications however, saving data using the shelve module is the preferred way to save variables to a file.

Only basic data types such as integers, floats, strings, lists and dictionaries can be written to a file as simple text.
File objects, for example, cannot be encoded as text.
"""











"""
########################################################################################################################
##########################################    working with alt file types    ###########################################
########################################################################################################################
.json .csv .jpg (and other image formats)

I would eventually need to learn, especially .json in receiving a payload through sql / python
"""



"""
###############################################   working with images   ################################################

mode as 'rb', to read binary, and write binary
"""

with open('keanu.jpg', 'rb') as rf:
    with open('keanu_2.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)
# this copies an image


with open('keanu.jpg', 'rb') as rf:
    with open('chonkeanu.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
# you can also copy with chunks





