#! usr/bin/env python3
# quizgen.py - random MCQ generating script

"""
- Creates 35 different quizzes
- Creates 50+ MCQ questions for each quiz, in random order.
- Provides the correct answer and three random wrong answers for each queston, in random order
- Writes the quizzes to 35 text files.
- Writes the answer keys to 35 text files.
"""

import random
import os
import pprint


# change directories
os.mkdir(os.getcwd() + '/quiz_files')
os.chdir(os.getcwd() + '/quiz_files')



# quiz data, keys are states and values are their capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
   'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


# generate 35 quiz files.

for quiz_num in range(35):
    ## create the quiz and answer key files
    quiz_file = open(f'capitalsquiz {quiz_num + 1}.txt', 'w')
    answer_file = open(f'capitalsquiz_answers {quiz_num + 1}.txt', 'w')

    ## Write out the header for the quiz
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write(f'State Capitals Quiz (Form {quiz_num + 1})'.center(79, " "))
    quiz_file.write('\n\n')

    ## shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    ## Loop through all 50 staes, making a question for each.
    for question_num in range(50):

      # get right and wrong answers;
      correct_answer = capitals[states[question_num]]
      wrong_answers = list(capitals.values())
      del wrong_answers[wrong_answers.index(correct_answer)]
      wrong_answers = random.sample(wrong_answers, 3)
      answer_options = wrong_answers + [correct_answer]
      random.shuffle(answer_options)

      #write questions and answers options to quiz quiz file
      quiz_file.write(f'{question_num + 1}: what is the capital of {states[question_num]}?\n')
      for option in range(4):
        quiz_file.write(f'   {"ABCD"[option]}. {answer_options[option]}\n')
      quiz_file.write('\n')

      #write answer key to corresponding answer file
      answer_file.write(f'{question_num + 1}. {"ABCD"[answer_options.index(correct_answer)]}\n\n')

    quiz_file.close()
    answer_file.close()












"""
########################################################################################################################
##################################################   personal notes   ##################################################
########################################################################################################################

New bits learned
random.sample(list, number_of_samples)
random.shuffle(list)
"""
