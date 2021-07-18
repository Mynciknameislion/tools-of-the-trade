
#Checks if a string can be turned to an int by using the int() function on it, returns true if it can, false if not
def intable(InString):
    InList = []
    InList += InString
    listLength = len(InList)

    for x in range(listLength):

        if(InList[x] == "1"):
            pass
        elif(InList[x] == "2"):
            pass
        elif (InList[x] == "3"):
            pass
        elif (InList[x] == "4"):
            pass
        elif (InList[x] == "5"):
            pass
        elif (InList[x] == "6"):
            pass
        elif (InList[x] == "7"):
            pass
        elif (InList[x] == "8"):
            pass
        elif (InList[x] == "9"):
            pass
        elif (InList[x] == "0"):
            pass
        else:
            return False
    return True


#Prints a list which is given to it to the python output
def printList(list, doNumberToLeft, numberInterval):
    internalList = []
    internalList += list
    listLength = len(internalList)
    currentInterval = numberInterval
    interval = numberInterval
    if(interval < 1):
        interval = 1
    if(doNumberToLeft == False):
        for x in range(listLength):
            print(internalList[x])
    else:
        for x in range(listLength):
            print(str(currentInterval), internalList[x])
            currentInterval += interval


#Inverts the list given to it
def invertList(list):
    newList = []
    itemAmount = len(list)

    for x in range(itemAmount, 0, -1):
        newList.append(list[x - 1])
    return newList


#Merges all items of a list to a string
def toString(list, separator):
    internalList = []
    internalList += list
    tempString = ""
    listLength = len(list)

    for x in range(listLength):
        tempString += str(internalList[x])
        if(x != listLength - 1):
            tempString += str(separator)
    return tempString


#Takes a string and separator and splits it into different items in a list
def toList(string, separator):
    internalSeparator = []
    internalSeparator += separator
    internalInput = []
    internalInput += string
    internalInput
    inputLength = len(internalInput)
    sepLength = len(internalSeparator)
    tempList = []
    inputCharCount = 0
    sepCharCount = 0
    tmpString = ""
    tmpStringTwo = ""
    while(inputCharCount < inputLength):
        if(sepCharCount == sepLength):
            tempList.append(tmpString)
            sepCharCount = 0
            tmpString = ""
            tmpStringTwo = ""
        if(internalInput[inputCharCount] != internalSeparator[sepCharCount]):
            tmpString += tmpStringTwo
            tmpString += internalInput[inputCharCount]
            tmpStringTwo = ""
            sepCharCount = 0
            inputCharCount += 1
        else:
            tmpStringTwo += internalInput[inputCharCount]
            sepCharCount += 1
            inputCharCount += 1
        if(inputCharCount == inputLength):
            tempList.append(tmpString)
            tmpString = ""
            tmpStringTwo = ""
    return tempList


#Takes a string or list and another and if it finds matching items from the second list in the first it flags them
def whiteListCompare(input, whitelist, aditionalFLags):
    newInStr = ""
    newWhite = []
    caseSensitive = False
    internalIn = []
    whiteLength = len(whitelist)
    matchList = []

    for x in aditionalFLags:
        if(x == "C"):
            caseSensitive = True
        else:
            pass

    if (caseSensitive != True):
        newInStr = input.lower()
        tempStr = toString(whitelist, "|")
        tempStr = tempStr.lower()
        newWhite = toList(tempStr, "|")
    elif(caseSensitive == True):
            newWhite = whitelist
            newInStr = input

    internalIn += newInStr
    currentChar = 0
    whiteChar = 0
    length = len(internalIn)
    for y in range(whiteLength):
        tempWhite = []
        tempWhite += newWhite[y]
        while(1 == 1):
            if(whiteChar == len(tempWhite)):
                matchList.append(True)
                whiteChar = 0
                currentChar = 0
                break
            elif(currentChar == length):
                matchList.append(False)
                whiteChar = 0
                currentChar = 0
                break
            elif(internalIn[currentChar] != tempWhite[whiteChar]):
                whiteChar = 0
                currentChar += 1
            else:
                currentChar +=1
                whiteChar += 1
    return matchList

