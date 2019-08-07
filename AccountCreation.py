from SaveMoneyDAO import *

moneydata = SaveMoneyDAO()


def defaultNewUser():
    print("What percentage of income input would you like to save? "
          "Enter as percentage not decimal.")
    savingsPercent = float(input())

    while(savingsPercent < 0 or savingsPercent > 100):
        print("Sorry the percentage entered: " + str(savingsPercent)
              + "is invalid")
        print("Please enter again")
        savingsPercent = float(input())

    # save the user information, need a percent field and amount field to save
    # both information
    moneydata.setField("savings", { "amount":0, "percent":savingsPercent })
    moneydata.setField("freeToSpend", {"amount":0, "percent":100 - savingsPercent})

def personalizedNewUser():
    # used to make sure user doesn't save more then or less then 100
    percentageLeft = 100

    # use a map to relate back to percentages and what fields have been added so far
    savingsPoolNames = {}

    # First pool name
    print("What would like to call your first savings pool?")
    print("An example would be LifeSavings.")
    savingsPoolName = input()

    # on blank input
    while not savingsPoolName:
        print("Please enter a valid savings pool name")
        savingsPoolName = input()


    # Second pool name
    print("What percent of your income would you like to save into "
          + savingsPoolName)
    print("Please make sure you enter a percentage and not a decimal")
    savingsPoolPercentage = float(input())


    # make sure percentage is valid
    while savingsPoolPercentage < 0 or savingsPoolPercentage > percentageLeft:
        print("The entered percent: " + str(savingsPoolPercentage) + "is invalid")
        print("Please enter again")
        savingsPoolPercentage = float(input())

    # Save data
    moneydata.setField(savingsPoolName, {"amount":0, "percent":savingsPoolPercentage})
    percentageLeft -= savingsPoolPercentage
    savingsPoolNames[savingsPoolName] = savingsPoolPercentage

    # Entering more pools
    while percentageLeft > 0:
        print("What would you like to call the next pool?")
        print("You still need to assign " + str(percentageLeft) + " of your income.")
        print("Type q if done")
        savingsPoolName = input()

        # check if already entered, if so prompt to update or not
        while savingsPoolName in savingsPoolNames.keys():
            print("you have already assigned this pool a percentage of "
                  + str(savingsPoolNames[savingsPoolName]))
            print("Would you like to overwrite? (y/n)")
            choice = input()
            if choice is "y" or choice is "Y":
                percentageLeft += savingsPoolNames[savingsPoolName]
                break
            else:
                savingsPoolName = input()
        if savingsPoolName is 'q':
            return
        print("What percent of your income would like to save into "
              + savingsPoolName)
        savingsPoolPercentage = float(input())

        # Check if entered percentage is valid
        while savingsPoolPercentage > percentageLeft or savingsPoolPercentage < 0:
            print("Invalid percentage, you have " +
                  str(percentageLeft) + " to assign and tried to assign "
                  + savingsPoolPercentage)
        percentageLeft -= savingsPoolPercentage
        moneydata.setField(
            savingsPoolName, {"amount":0, "percent":savingsPoolPercentage})
        print("Successfully added!")


