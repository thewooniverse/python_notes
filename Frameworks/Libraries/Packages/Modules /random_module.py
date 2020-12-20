import random
# you should not use this for password or cryptography
# for that, you can look into secrets module

# random and uniform methods
# random method to get random floating value from 0 to 1;
# 0 is inclusive and 1 is not.
# print(random.random())
# print(random.uniform(1, 10))
# also returns random fl value from 1, 10.
# not really that useful.

dice_result = random.randint(1, 6)
print(dice_result)
# returns random integer, pretty useful.
# lots of use cases like coinflip or dice.

greetings = ['Hi', 'Hey', 'Heyy', 'Howdy', 'Hola']
colors = ['Red', 'Black', 'Green']
choice = random.choice(greetings)
results = random.choices(colors, weights=[18, 18, 2] ,k=10)
print(choice)
print(results)
# here choices selects multiple times, as many times as defined in k
# and choice simply selects one.
# in the colors of the roulette example, you can actually set weights of the colors
# because the likelihood of Red, and Black may be very different from Green
# this is done by the weights kwarg.
# red has 18/38 chance, so does black and green has 2/38.


deck = list(range(1, 53))
random.shuffle(deck)
print(deck)
# this shuffles the list passed as the argument to the method

hand = random.sample(deck, k=5)
print(hand)
# this returns a random unique sample of k=5 cards from the deck defined
