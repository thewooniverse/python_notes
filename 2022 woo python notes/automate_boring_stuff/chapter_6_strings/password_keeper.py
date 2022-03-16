#! python
# password_keeper.py - 1. a password keeper with encryption logic 2. also a practice project
# developed by thewooniverse
"""
References:
https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password
"""


import sys, pyperclip, os, csv
# import encryption and decryption from cipher.py


# load encrypted passwords from separate pw.csv file
cwd = os.getcwd()

# check if pw.csv is in respective directory
# if not, create one with the right headers

dir_ls = os.listdir(cwd)
if 'pw.csv' not in dir_ls:
    with open('pw.csv', 'w') as output_csv:
        fields = ['account', 'password']
        output_writer = csv.DictWriter(output_csv, fieldnames=fields)
        output_writer.writeheader()

else:
    pass

# read the csv file, and populate the list of accounts stored in the file currently
account_ls = []

with open('./pw.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        account_ls.append(row['account'])




# define functions to get and set password from cipher.py module
def get_password(account, pin):
    pass


def set_password(account, pin, password):
    pass





### user prompts ###
if len(sys.argv) < 2:
    print("""USAGE:
        python password_retriever.py get [account] [PIN] - copy account password decrypted with PIN
        python password_retriever.py set [account] [PIN] [password]- copy account password encrypted with PIN

        ** set command will allow you to overwrite existing passwords
        ** retrieving an existing account with the incorrect PIN will return a password that may be incorrectly decrypted
        """)
    sys.exit()


# assign args passed by user to variables
acct = sys.argv[2]
pin_num = sys.argv[3]
if sys.argv[0] == set:
    new_pw = sys.argv[4]
else:
    pass


# call the functions based on the sys.argvs
if sys.argv[1] == "get":
    if acct in account_ls:
        print("account found, retrieving password unlocked by PIN!")
    else:
        print("account not found, try setting a new password!")


elif sys.argv[1] == "set":
    print("GETTING")












# if account in PASSWORDS:
#     # in in py dicts will look for the keys anyway;
#     pyperclip.copy(PASSWORDS[account])
#     print(f"Password for {account} copied to clipboard")

# else:
#     print(f"There is no account called {account} in our database!")



