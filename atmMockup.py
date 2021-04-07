import datetime
import random

now = datetime.datetime.now()

database = {}

#Initialization

def init():
    print('Date:', now.strftime("%a %d/%m/%y %H:%M:%S"))
    print("Welcome to the first Bank in the Wolrd")

    selectedOption = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if (selectedOption == 1):
        login()

    elif (selectedOption == 2):
        register()

    else:
        print("You have selected invalid option")
        init()


#user login : account number and password
def login():
    print("********* Login ***********")

    userAccountNumber = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber, userDetails in database.items():
        if (accountNumber == userAccountNumber):
            if (userDetails[3] == password):
                bankOperation(userDetails)

    print('Invalid account or password')
    login()


#user registration: first_name, last_name, email, password,accountNumber
def register():

    print("****** Register *******")

    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    email = input("What is your email address? \n")
    password = input("create a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()

#Bank operations
def bankOperation(user):
    print('Date:', now.strftime("%a %d/%m/%y %H:%M:%S"))
    print("Welcome %s %s " % (user[0], user[1]))

    selectedOption = int(input("What would you like to do?\n (1) deposit\n (2) withdrawal\n (3) Logout\n (4) Exit \n"))

    if (selectedOption == 1):

        depositOperation()
    elif (selectedOption == 2):

        withdrawalOperation()
    elif (selectedOption == 3):

        logout()
    elif (selectedOption == 4):

        exit()
    else:

        print("Invalid option selected")
        bankOperation(user)


#random generate account number
def generationAccountNumber():
    return random.randrange(11111111,99999999)

#withdrawalOperation
def withdrawalOperation():
    amount = int(input("How much would you like to withdraw? \n"))
    print('Take Your Cash: %d$' % amount)

#depositOperation
def depositOperation():
    amount = int(input("How much would you like to deposit? \n"))
    print('Your balanse Is: %d$' % amount)

#logout
def logout():
    login()


init()