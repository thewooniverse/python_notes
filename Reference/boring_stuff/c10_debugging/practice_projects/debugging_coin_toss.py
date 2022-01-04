

import random, logging, sys
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

logging.debug('start of program\n')

guess = ''
tries = 0

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails: ')
    guess = input()

tries += 1

toss = random.randint(0, 1) # 0 is tails, 1 is heads

if toss == 0:
    toss = 'tails'
elif toss == 1:
    toss = 'heads'



while tries < 2:
    
    if toss == guess:
        print('you got it!!')
        sys.exit()

    elif toss != guess:
        print('nope, try again\n')
        print('Guess the coin toss! Enter heads or tails: ')
        guess = input()
        tries += 1

if toss == guess:
    print('you got it!!')
    sys.exit()
    

print('nope...')
print("all tries used... you're really bad haha")





"""
Bug 1;
type toss is an int, and is not heads or tails in string.
it can never match or be equal to user's input even if they are right.
Resolution 1;
convert the toss to a string corresponding to the comment.


"""
