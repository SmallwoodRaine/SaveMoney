from SaveMoneyDAO import *
moneyDAO = SaveMoneyDAO()
moneyData = moneyDAO.getMoneyData()

def addNewIncome():
    print("Please enter the income amount.")
    newIncome = float(input())
    for key in moneyData.keys():
        percentage = float(moneyData[key]["percent"]) / 100.0
        moneyData[key]["amount"] += newIncome * percentage
    moneyDAO.setData(moneyData)
    print("Added changes successfully")

def displayAmounts():
    for key in moneyData.keys():
        print(str(key) + ": $" + str(moneyData[key]["amount"]))