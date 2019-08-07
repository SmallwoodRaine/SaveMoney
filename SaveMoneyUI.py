from SaveMoneyDAO import *
from AccountCreation import *
from ReturningUserHandler import *
"""
SaveMoneyUI will hand all the UI funcitonality of the SaveMoney application.
"""
MONEYDATA = SaveMoneyDAO()

# initiates the application
def startSaveMoneyApplication():
    displayIntroductionUI()

# prints the introduction UI, which will be different for new vs returning users
def displayIntroductionUI():
    # Determine if user is returning or not by checking if moneyData.json
    # is empty or not
    if MONEYDATA.isEmpty():
        displayNewUserUI()
    else:
        displayReturningUserUI()


def displayNewUserUI():
    print("Hello, welcome to an easy, fast, and intuitive "
          "money saving application")
    print("This application will eliminate the need to have multiple bank"
          " accounts for the purpose of managing money.\n")
    print("Please choose an option below")
    print("(1). Setup using defaults(Savings, and freeToSpend money). "
          "You Can always change this later.")
    print("(2). Personalize your own savings pools.")
    print("(q). Quit the application.")
    userChoice = input()
    handleNewUserChoice(userChoice)

def handleNewUserChoice(userInput):
    if userInput is '1':
        defaultNewUser()
    elif userInput is '2':
        personalizedNewUser()
    elif userInput is 'q':
        print("Goodbye mate")
        return
    else:
        print("Invalid input please try again")
        displayNewUserUI()

def displayReturningUserUI():
    menuChoice = '0'
    while menuChoice is not 'q':
        print("Hello, welcome back bud")
        print("Please enter a choice below")
        print("(1) Input income")
        print("(2) Display current amounts in each pool")
        print("(3) Settings")
        print("(q) Quit")
        menuChoice = input()
        handleReturningUserChoice(menuChoice)

def handleReturningUserChoice(userInput):
    if userInput is '1':
        addNewIncome()
    if userInput is '2':
        displayAmounts()