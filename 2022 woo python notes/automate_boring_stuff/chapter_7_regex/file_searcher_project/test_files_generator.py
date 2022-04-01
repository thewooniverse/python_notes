#! python3
"""
test_files_generator.py - generates a bunch of test files in ./test_files directory
as part of a practice project. Each populated file will have random texts OR emails
"""

import random
import traceback
import logging
import os

# logging config
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('start of program!')


# create a bunch of random texts:
emails = ["random.com", 'word.net', 'woowoo.co',
          'nothingness.void', 'void.net', 'swarm.wtf', 'civ5.com']
names = ['mcfiffer', 'dillydally', 'mcjooson',
         'mcfeffer', 'garwarbabglg', 'murloc_king', 'yogi_bhajan', 'bhagwan', 'lmfao']
words = ['yadyadyaydayadydaydaa', 'yogajbiaja',
         'gibberish', 'lots of gibberish', 'lotsacrap', 'asdf']

# create files
test_path = os.getcwd()+os.path.sep+'test_files'
logging.debug(test_path)
assert os.path.isabs(test_path)

for n in list(range(1, 100)):
    with open(f'{test_path+os.path.sep}{n}.txt', 'w') as test_file:
        bogus = random.choice([True, False])
        if bogus:
            bogus_word = random.choice(words)
            test_file.write(bogus_word)
            logging.debug(f'adding bogus {bogus_word}')

        else:
            random_email = random.choice(names) + "@" + random.choice(emails)
            test_file.write(random_email)
            logging.debug(f'adding random email {random_email}')
