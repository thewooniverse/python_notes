#! python
# password_keeper.py -
# developed by thewooniverse

import sys, pyperclip, os

# import encryption and decryption from cipher.py


# load encrypted passwords from separate pw.csv file
cwd = os.getcwd()


### user prompts ###
if len(sys.argv) < 2:
    print("""USAGE:
        python password_retriever.py get [account] [PIN] - copy account password decrypted with PIN
        python password_retriever.py set [account] [PIN] [password]- copy account password encrypted with PIN
        """)
    sys.exit()



account = sys.argv[1]
pin = sys.argv[2]
try:
    password = sys.argv.[3]
except:
    pass



if account in PASSWORDS:
    # in in py dicts will look for the keys anyway;
    pyperclip.copy(PASSWORDS[account])
    print(f"Password for {account} copied to clipboard")

else:
    print(f"There is no account called {account} in our database!")
