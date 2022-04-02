#! python
import random
import logging
import traceback
import os

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('start of program!')


guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()
assert guess in ('heads', 'tails')

toss = random.randint(0, 1)  # 0 is tails, 1 is heads

if toss == 0:
    toss = 'tails'
elif toss == 1:
    toss = 'heads'
assert toss in ('heads', 'tails')


while toss != guess:
    print("Nope - guess again!")
    guess = input().lower()
    while guess not in ('heads', 'tails'):
        guess = input().lower()

if toss == guess:
    print("you got it :D")

try:
    raise Exception('This is a detailed error message')
except:
    errorFile = open(f'{os.getcwd()+os.path.sep}cointoss_errorlog.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to cointoss_errorlog.txt')
