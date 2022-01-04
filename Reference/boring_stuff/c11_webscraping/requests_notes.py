#! /usr/bin/python

"""
########################################################################################################################
#############################   Downloading files from the web with the requests module   ##############################
########################################################################################################################

The requests module lets you easily download files from the Web without having to worry about complicated issues such
as network errors, connection problems and data compression.
The requests module doesn't come with Python, so you'll have to install it first.

    So you'll need to install it with;
    pip install requests

The requests module was written because Python's urllib2 module is too complicated to use.
In fact, take a permanent market and black out this part about urllib2 entirely, and forget it was mentioned.
If you ever need to download things from the Web, just use the requests module.

"""

import requests


"""
The requests.get() function takes a string of a URL to download.
By calling type() on requests.get()'s return value, you can see that it returns a Response object (elaborated later),
which contains the response that the web server gave for your request.
"""

res= requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))
# took some time to load, but creates a Response object;
# <class 'requests.models.Response'>

print(res.status_code == requests.codes.ok)
# prints True

print(len(res.text))
# prints 179380

print(res.text[:250])


"""
The URL goes to a text web page for the entire play of Romeo and Juliet provided by Projec Gutenberg.

You can tell that the requests for this web page succeeded by checking the status_code attribute of the Response object.
If it is equal to the value of requests.codes.ok then everything went fine.
( Incidentally, the status code for "OK" in HTTP protocol is 200, you may already be familiar with a similar 404 status code for "NOT FOUND"

If the request succeeded the downloaded web page is stored as a string in the Response object's text variable.
This variable holds a large string of the entire play;
The call to len(res.text) shows that you it is mor than 178000 characters long.

Finally, calling print(res.text[:250]) displays the first 250 characters

"""




"""
###############################################   checking for errors   ################################################

As you've seen, the Response object has a status_code attribute that can be checked against the requests.codes.ok
to see whether the download succeeded.
A simpler way to check for success is to call the raise_for_status() method on the Response object.
This will raise an exception if there was an error downloading the file and will do nothing if the download succeeded.
"""

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
# res.raise_for_status()

# prints a traceback that ends with;
# requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://inventwithpython.com/page_that_does_not_exist

"""
The raise_for_status() method is a good way to ensure that a program halts if a bad download occurs.
This is a good thign: You want your program to stop as soon as some unexpected error happens.
If a failed download isn't a dealbreaker for your program, you can wrap the raise_for_status() line with try and except
statements to handle this error case without crashing.
"""

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem %s' % (exc))
# There was a problem 404 Client Error: Not Found for url: http://inventwithpython.com/page_that_does_not_exist

"""
Always call raise_for_status() after calling requests.get().
You wan to be sure that the download has actually worked before your program continues.
"""







"""
####################################   Saving Downloaded files to the hard drive   #####################################

You can save the web page to a file on your hard drive with the standard open() function and write() method.
There are some slight differences though.
First you must open the file in write binary 'wb' mode as the secondary arg of open().
Even if the parge is in plaintext (like Romeo and Juliet above), you need to write binary instead of text data in order
to maintain the Unicode Encoding of the text.

    Visit for a primer on unicode
    http://www.joelonsoftware.com/articles/Unicode.html
    http://nedbatchelder.com/text/unipain.html


"""


res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
play_file = open('Romeo_and_Juliet.txt', 'wb')
for chunk in res.iter_content(100000):
    play_file.write(chunk)

play_file.close()


"""
The iter_content() method returns "chunks" of the content on each iteration through the loop.
Each chunk is of the bytes data type, and you get to specify how many bytes each chunk will contain.
On hundred thousand byes is generally a good size, so pass 100000 as the argument for iter_content()

The file now exist in the current workign directory.
Note that while the filename on the website was pg1112.txt, the file on your harddrivei s a different name.
The requests module simply handles downloading the contents of web pages.
One the page is downloaded, it is simply data in your program.
Even if you lose your inernet connection after downloading the webpage, the page data would still be on your computer.

The main reason why iter_content() stuff exist is to ensure that the requests module doesn't eat up too much memory even if you download
massive files. YOu can learn about the requests module's other features below;

- http://requests.readthedocs.org/

"""
