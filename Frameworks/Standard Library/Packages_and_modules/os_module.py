import os
from datetime import datetime

os.chdir('./working_with_json')
print(os.getcwd())
print(os.listdir())

# os.chdir('/Users/joowo/Desktop/Python/Coding Practice/School and textbook/')
# os.chdir changes directory to defined arg
# seems there is something up with Windows / and \.

# print(os.getcwd()), getcwd returns current working directory
# print(os.getcwd())

# print(os.listdir('dir'))
# os.listdir() returns the files in the defined directory
# Which by default is the current working directory.
# must be in '' marks.


# os.mkdir('YouTube lectures')
# os.mkdir('School and textbook')
# os.makedirs('directories/sub-directories')
# mkdir and makedirs are pretty similar but makedirs
# but makedirs supports sub-directories;

# similarly, there are rmdir(directory) and
# os.removedirs('directories/sub-directories')
# which again support sub-level directories removal.


# os.rename('abc.py', 'cde.py')
# os.rename('Buddy Engine', 'Censorship Engine')
# Works with all file types and directories;
# syntax is original filename, new filename.


# print(os.stat('cde.py'))
# os.stat(file), few things get printed out.
# see documentation online to see in detail.
# st_size = size in bytes.
# which you can then target with os.stat('file').st_size
# st_mtime, is a timestamp, which you can readable format with the datetime module below.
# mod_time = os.stat('cde.py').st_mtime
# print(datetime.fromtimestamp(mod_time))
# st_mtime=1582486520 turns into 2020-02-23 19:35:20.235463
# can be really useful for web applications for files that update frequently;


# In order to traverse the directory and see the entire directory tree and its files.
# We can use the os.walk() method.
# generator that yields a tuple of 3 values as it walks the directories;
# each directory that it sees;
# yields - directory path, directories in that path and the files in that path.
# for dirpath, dirnames, filenames in os.walk('/Users/joowo/Desktop/Python/'):
#    print('current path: ', dirpath)
#    print('directories: ', dirnames)
#    print('files: ', filenames)

# you pass the root path that you want to walk down from;



# print(os.environ)
# In windows you don't have a HOME env variable (which captures the home dir)
# So its USERPROFILE, but anyway...
# the method os.environ returns environment variables in a dict format.
# os.environ.get('env_var') returns the value set for that specific variable;

# file_path = os.path.join(os.environ.get('USERPROFILE'), 'test.txt')
# os.path.join - takes two arguments
# os.path.join takes out the confusion around the / and //s.
# We will explore file creation in another practice session with file objects;
# which together can then be stacked to create a more complex downloads file org.
# print(file_path)


print(os.path.basename('/Users/joowo/Desktop/test.sh'))
# returns test.sh
print(os.path.dirname('/Users/joowo/Desktop/test.sh'))
# returns /Users/joowo/Desktop

print(os.path.split('/Users/joowo/Desktop/test.sh'))
# returns ('/Users/joowo/Desktop', 'test.sh')
# returns desktop as 2nd value in returned tuple if file at the end doesn't exist;
# ie - it returns to last filename or directory
# also note, that a test.sh and /bogus/ doesn't exist, but still it runs;

print(os.path.exists('/Users/joowo/Desktop/bogus')) # returns False
print(os.path.exists('/Users/joowo/Desktop')) # returns True
print(os.path.isdir('/Users/joowo/Desktop')) # returns True
print(os.path.isfile('/Users/joowo/Desktop')) # returns False
# a lot of these are very intuitive...

print(os.path.splitext('Desktop/test.sh'))
# much easier to do this than to do string splicing, to split of the ext.
print(os.path.splitext(os.path.basename('Desktop/test.sh')))

print(dir(os.path))
# To look at all the possible methods for os.path.

