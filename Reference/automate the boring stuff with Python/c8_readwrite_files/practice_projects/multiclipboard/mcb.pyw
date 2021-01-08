#! usr/bin/env Python3
# multiclipboard - mcb.pyw, a handy tool for copying multiple items in your clipboard

"""
mcb.pyw - Saves and loads pieces of text to the clipboard.
Usage: Python mcb.pyw save <keyword> - Saves clipboard to keyword.
       Python mcb.pyw <keyword> - Loads keyword to clipboard.
       Python mcb.pyw list - Loads all keywords to clipboard.
       Python mcb.pyw delete <keyword> - deletes keyword from multiclipboard
       Python mcb.pyw clear - deletes all keywords from clipboard

.pyw extension means that Python won't show a terminal window when it runs a program.

"""

# import modules
import sys, pyperclip, shelve, os

# open mcb
mcb_shelf = shelve.open('mcb')




# read sys argv to determine what needs to be done and do it

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save': # if the keyword is save
    mcb_shelf[sys.argv[2]] = pyperclip.paste() # save this data, overwrites if it exists.

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    mcb_shelf.pop(sys.argv[2])
    print('deleted from clipboard')


elif len(sys.argv) == 2:

    if sys.argv[1] == 'list':
        print('Below are the keywords and their saved values available:\n')
        for item in list(mcb_shelf.items()):
            print(f'Keyword: {item[0]}\nContent: {item[1]}\n\n')

    elif sys.argv[1] == 'clear':
        mcb_shelf.clear()
        print('clipboard cleared')

    else:
        try:
            print(f'copied {sys.argv[1]} to clipboard')
            pyperclip.copy(mcb_shelf[sys.argv[1]])
        except:
            print('Error message, this keyword does not exist, use the "list" keyword to see the list of all saved keywords')



# close file
mcb_shelf.close()



