#! python3
"""
rand_text_gen.py - populates ./test_files directory with a bunch of text files full of random
texts, however, sometimes each different sentence will have a double space error inside them.

"""
#import modules
import os
import random
import logging

# set up logging configs
logging.basicConfig(level=logging.DEBUG, filename=f'{os.getcwd()+os.path.sep}error_logs{os.path.sep}rand_text_gen_log.txt',
                    format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug(f'\nstart of program---!')

# open files to populate randomness word fields + set up double spaces
spaces = [' ', '  ', '. ']
spaces_dist = random.choices(spaces, weights=[0.8, 0.1, 0.1], k=100)
sc = spaces_dist.count(' ')
logging.debug(f'the nubmer of spaces out of 100 is {sc}')


# get random words from randon_texts.txt (random text dump)
test_files_abs_dir = os.getcwd() + os.path.sep + 'test_files'
rf = open(os.getcwd()+os.path.sep+'rand_texts.txt')
read_text = rf.read()
rand_texts = list(set(' '.join(read_text.split('\n')).split(' ')))
rf.close()
logging.debug(rand_texts)

# create 10 files with random texts of 100 words, randomly joined by . and spaces
for n in list(range(1, 10)):
    selected_words = random.choices(rand_texts, k=100)

    with open(f'{test_files_abs_dir+os.path.sep}test_{n}.txt', 'w')as test_file:
        words = [selected_words.pop()]
        while selected_words:
            popped_word = [selected_words.pop()]
            space_choice = random.choice(spaces_dist)
            words = [space_choice.join(popped_word + words)]
        logging.debug(words[0])

        test_file.write(f'Test File {n}. ' + words[0])
