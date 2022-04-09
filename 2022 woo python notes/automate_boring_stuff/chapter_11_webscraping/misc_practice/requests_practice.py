#! python3
"""
requests practie notes
"""

# import modules
import requests
import logging
import os

# configure subfiles for error logging
directories = ["error_logs"]
for directory in directories:
    try:
        os.makedirs(os.getcwd()+os.path.sep+directory)
    except FileExistsError:
        pass

basename = os.path.basename(__file__).split('.')[0]
logging.basicConfig(level=logging.DEBUG,
                    filename=f"{os.getcwd()+os.path.sep}error_logs{os.path.sep+basename}.txt", format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug(f'\n---start of program---!')

# begin script
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
logging.debug(res)
logging.debug(type(res))
logging.debug(res.status_code == requests.codes.ok)
logging.debug(len(res.text))
logging.debug('\n'+res.text[:333])

logging.debug(f'\n///end of program///')


res2 = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res2.raise_for_status()
except Exception as exc:
    logging.debug(f'There was a problem {exc}')


# saving content from the web to your harddrive
try:
    os.makedirs(f'.{os.path.sep}downloads')
except FileExistsError:
    pass

play_file = open(
    f'.{os.path.sep}downloads{os.path.sep}romeo_and_juliet.txt', 'wb')
for chunk in res.iter_content(100000):
    play_file.write(chunk)


"""
that's pretty much it to the requests module:
You're playing with response objects as seen above;
and you got the open() write() close() workflow for writing to files.
You also have the for loop and iter_content() stuff that you can use too :)


"""
