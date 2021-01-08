# File objects - Corey Schafer + Code Academy

import os
import json
import csv
# below is from old windows notes
# os.chdir('/Users/joowo/Desktop/Python/Coding Practice/YouTube Lectures/files')


#f = open('test.txt', 'r')
# if you're working with files from different directories
# you're gonna have to pass the path of that file to the open command
# this is assuming test.txt is in the
# open command allows us to specify whether we are opening the file for...
# reading ('r'), writing('w'), appending('a'), reading and writing('r+').
# default is opening for reading.

# print(f.name)
# print(f.mode)

# f.close()
# this is necessary when you open files without a context manager (with)
# if we don't close the file, we may run into leaks and other problems.


# context manager
with open('/Users/joowo/Desktop/cage.txt', 'r') as f:
    f_contents = f.read()
    # print(f_contents)

# context managers allows us to work with the file within the block
# and it automatically closes the files.
# so considered best practice
# we can still access after the variable f like with
# print(f.closed)
# but you are not able to read the file because it is closed and it will throw an error.




with open('/Users/joowo/Desktop/cage.txt', 'r') as f:
    f_line1 = f.readline()
    #print(f_line1, end='')
    # prints ABC
    f_lines = f.readlines()
    # print(f_lines)
    # prints ALL lines in a list format
    # again, lines also gets the NEXT line, so it gets everything from ABC onwards
    f_line = f.readline()
    # print(f_line)
    # f.readline() gets the NEXT line in our file, so the f_line here is not equal to anything.
    # as it is called after the f.readlines()
    # read just returns an empty string when it reaches the end of the file.


with open('/Users/joowo/Desktop/cage.txt', 'r') as f:
    # for line in f:
    #    print(line, end='')
    pass


# with open('/Users/joowo/Desktop/cage.txt', 'r') as f:
    #size_to_read = 10
    #f_c = f.read(size_to_read)
    # this shows us where we are at
    # while len(f_c) > 0:
    #print(f_c, end='*')
    # you can see clearly that its reading 10 char at a time and how end="*" works
    #f_c = f.read(size_to_read)


with open('/Users/joowo/Desktop/cage.txt', 'r') as f:
    print(f.tell())
    # f.tell() shows you the position that we are currently read into
    # this prints 0
    size_to_read = 3
    f_contents = f.read(size_to_read)
    print(f_contents)
    print(f.tell())
    # at this point f.tell prints 3

    f.seek(0)
    # f.seek allows us to point where we are in a file to a specific location

    f_contents = f.read(size_to_read)
    print(f_contents)
    print(f.tell())

    f_contents = f.read(size_to_read)
    print(f_contents)
    print(f.tell())


### writing ###

# with open('test.txt', 'w') as f:
    # f.write('Test')
    # f.seek(0)
    # by havign f.seek(0) here, we overwrite 'test' in the same location in test.txt
    # without it files.txt would be 'TestTest'
    # f.write("ABC")
    # if test.txt exists it will overwrite it
    # if test.txt does not exist it will create it.
    # to add to it / append, open with 'a'

    # write only over-writes what is necessary;
    # so that if the second f.write is ("ABC") then test.txt will be;
    # ABCt, as writing ABC only needs 3 characters, so it doesn't over write t.


### applied ###

# copy paste function
with open('/Users/joowo/Desktop/cage.txt', 'r') as rf:  # to stand for read-file
    with open('test_copy.txt', 'a') as wf:  # to stand for write file
        for line in rf:
            wf.write(line)

# this function opens a readfile, and within the block opens a write file as well.
# and iterates through every line in readfile, writes the line onto the wf
# calling the function again on 'w' overwrites / and creates the same copy over it.
# calling it with 'a', we append to the end of the file.


### working with image files ###

with open('love.jpg', 'rb') as rf:
    with open('love_copied.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)
# I can easily write these as a function


# we can also do this chunk by chunk instead of line by line
# like how we did for the text, with seek and size_to_read

with open('love.jpg', 'rb') as rf:
    with open('love_2.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


### working with CSV files ###

# print(dir(csv))

list_of_email_addresses = []
list_of_usernames = []

with open('test.csv', newline='') as csv_file:
    user_reader = csv.DictReader(csv_file)
    for row in user_reader:
        list_of_email_addresses.append(row['Email'])
        print(row)

# in a csv.dictreader, default delimiter is csv,
# but often times you will need to work with different delimiters like tabs.

with open('test2.csv', newline='') as csv_file:
    address_reader = csv.DictReader(csv_file, delimiter=';')
    for row in address_reader:
        print(row['Address'])

big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {
    'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}]


# again, this creates / overwrites in the same way as other files.
with open('test3.csv', 'w') as output_csv:
    fields = ['name', 'userid', 'is_admin']
    # defining the fields, this can also be done in many other ways
    output_writer = csv.DictWriter(output_csv, fieldnames=fields)
    # this INSTANTIATES our CSV writer OBJECT.
    # first arg is output_csv, which is the file handler object
    # second is fieldnames keyword parameter, and we passed the predefined fields

    output_writer.writeheader()
    # now we call the write header method to the writer object;
    # which writes all the fields passed to fieldnames to the first row in oru file.
    # and our csv file is ready to be written!

    for item in big_list:
        output_writer.writerow(item)
        # now for every item in big_lsit
        # we iterate and call the writer object's writerow method
        # and write each line into the csv file.


### working with JSON files ###


with open('test.json') as test_json:
    # since we are opening to read, we don't need to pass anything as it is default
    json_data = json.load(test_json)
    # json.load parses the json_data and creates a dictionary out of the file.

print(json_data['secret text'])


with open('newson.json', 'w') as json_file:
    json.dump(big_list, json_file)
    # json.dump() takes two arguments
    # first the data object
    # then the file object you want to save it as.


