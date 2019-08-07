import json
MONEYDATAFILENAME = "moneyData.json"

class SaveMoneyDAO:
    def __init__(self):
        # Pull the data from the json file
        with open(MONEYDATAFILENAME) as moneyDataFileFrom:
            if moneyDataFileFrom.read(3):
                with open(MONEYDATAFILENAME) as moneyDataFileFrom:
                    self._moneyData = json.load(moneyDataFileFrom)
            else:
                self._moneyData = {}

    #  getField is used to receive elements from the json file.
    def getField(self, fieldName: str):
        return self._moneyData[fieldName]

    # setField is used to set a new field in the json file
    def setData(self, newData:{}):
        with open(MONEYDATAFILENAME, 'w') as moneydataFile:
            json.dump(newData, moneydataFile)

    def setField(self, fieldName: str, fieldValue:{}):
        self._moneyData[fieldName] = fieldValue
        with open(MONEYDATAFILENAME, 'w') as moneyDataFileTo:
            json.dump(self._moneyData, moneyDataFileTo)

    # return a dictionary containing all the data
    def getMoneyData(self):
        return self._moneyData

    # determine if moneyData.json is empty or not
    def isEmpty(self):
        if not self._moneyData:
            return True
        else:
            return False