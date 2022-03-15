#! python
# password_keeper.py -
# developed by thewooniverse
"""
References:
https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password
"""




import sys, pyperclip, os
# import encryption and decryption from cipher.py




# load encrypted passwords from separate pw.csv file
cwd = os.getcwd()

# check if pw.csv is in respective directory
# if not, create one


# if yes, open








### user prompts ###
if len(sys.argv) < 2:
    print("""USAGE:
        python password_retriever.py get [account] [PIN] - copy account password decrypted with PIN
        python password_retriever.py set [account] [PIN] [password]- copy account password encrypted with PIN
        """)
    sys.exit()



# assign args passed by user to variables
account = sys.argv[1]
pin = sys.argv[2]
if sys.argv[0] == set:
    password = sys.argv[3]
else:
    pass










# if account in PASSWORDS:
#     # in in py dicts will look for the keys anyway;
#     pyperclip.copy(PASSWORDS[account])
#     print(f"Password for {account} copied to clipboard")

# else:
#     print(f"There is no account called {account} in our database!")
