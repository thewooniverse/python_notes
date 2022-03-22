#! python
"""
random_quiz_gen.py - creates multiple quizzes with questions and answers in random order along with its answer key
"""

import random, os

# check if directories exist
cwd = os.getcwd()
try:
        os.makedirs(cwd + os.path.sep + "quizzes")
except:
    pass
try:
    os.makedirs(cwd + os.path.sep + "answers")
except FileExistsError:
    pass



# import quiz data
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# generate 35 quizzes

for quiz_num in range(35):
    # TODO: Create the quiz and answer key files
    quiz_file = open(f".{os.path.sep}quizzes{os.path.sep}quiz{quiz_num + 1}.txt", 'w')
    ans_file = open(f".{os.path.sep}answers{os.path.sep}answer{quiz_num + 1}.txt", 'w')

    # TODO: Write out the header for the quiz
    quiz_file.write('US Capitals Pop Quiz!\n')
    quiz_file.write(f'\nName: {" "*15} Class: {" "*15}\n')
    quiz_file.write(f'\n{"_"*35}\n')

    # write ansewr file header
    ans_file.write('US Capitals Pop Quiz! - Answers!\n')
    ans_file.write(f'\n{"_"*35}\n')


    # TODO: Shuffle the order of the states
    states = list(capitals.keys())

    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each
    for state in states:
        choices = ['A', 'B', 'C', 'D']
        answer_choice = random.choice(choices)
        correct_answer = capitals[state]
        bogus_choices = []

        # create quiz for each state
        quiz_file.write(f'\n\n{states.index(state)+1}: what is the capital of {state}?\n')
        quiz_file.write(f'\n')
        ans_file.write(f'\n\n{states.index(state)+1}: what is the capital of {state}?\n')

        for choice in choices:
            # if it is the right answer, write the answer into both the ansewr and question sheet
            if choice == answer_choice:
                quiz_file.write(f"    {choice}. {correct_answer}\n")
                ans_file.write(f"Answer is {answer_choice}, {correct_answer}\n")

            # if its not the right answer
            else:
                possible_choices = list(capitals.values())
                bogus_choice = random.choice(possible_choices)

                while (bogus_choice in bogus_choices) and (bogus_choice == correct_answer):
                    print("found duplicate")
                    bogus_choice = random.choice(possible_choices)


                quiz_file.write(f"    {choice}. {bogus_choice}\n")
                bogus_choices.append(bogus_choice)
                print(bogus_choices)







