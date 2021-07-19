import openpyxl
import leosLib


# Here is where all the necessary excel documents are opened
transactionWorkbook = openpyxl.load_workbook("transaction-history.xlsx")
transactionSheet = transactionWorkbook["Transactions"]
balanceSheet = transactionWorkbook["Inventory"]

currentCell = transactionSheet.cell(row = 100, column = 100)
currentCellTwo = balanceSheet.cell(row=1, column=1)

def fillCell(row, collum, string):
    current_cell = transactionSheet.cell(row=row, column=collum)
    if(string != None):
        current_cell.value = str(string)
    else:
        current_cell.value = None

def fillCellTwo(row, collum, string):
    current_cell = balanceSheet.cell(row=row, column=collum)
    if(string != None):
        current_cell.value = str(string)
    else:
        current_cell.value = None

def readCellTwo(row, collum):
    current_cell = balanceSheet.cell(row=int(row), column=int(collum))
    if(current_cell.value != None):
        return str(current_cell.value)
    else:
        return None

def findFirstEmpty(checkedCollum):
    currentRow = 1
    current_cell = transactionSheet.cell(row=1, column=int(checkedCollum))
    while(current_cell.value != None):
        currentRow += 1
        current_cell = transactionSheet.cell(row = int(currentRow), column = int(checkedCollum))
    return currentRow

def findFirstEmptyTwo(checkedCollum):
    currentRow = 1
    current_cell = balanceSheet.cell(row=1, column=int(checkedCollum))
    while(current_cell.value != None):
        currentRow += 1
        current_cell = balanceSheet.cell(row = int(currentRow), column = int(checkedCollum))
    return currentRow

def reorganizeBalance():
    whitespaceLocale = findFirstEmptyTwo(3)
    currentRow = whitespaceLocale + 1
    while(readCellTwo(currentRow, 3) != None):
       for x in range(3, 7):
           tempString = readCellTwo(currentRow, x)
           fillCellTwo(currentRow - 1, x, tempString)
       currentRow += 1

    whitespaceLocale = findFirstEmptyTwo(3)
    whitespaceLocale -= 1
    for x in range(3, 7):
        fillCellTwo(whitespaceLocale, x, None)



validIn = False
usrIn = ""
main_actions_list = ["Buy an item (add it to the stock database)",
                     "Sell an item (remove it from the stock database)",
                     "Edit an entry of an item in the stock database (this is for if items are removed without being sold or if you entered a value wrong/need to edit TT or paid value of an entry",
                     "Add inventory (add inventory to your trading inventory, this is for of you got items from a non trading source and want the system to consider them)"]

# Welcome message
print("Welcome to your Entropia trade manager, from here you will be prompted to enter which action you wish for the program to do, hit enter to continue")
input("")

# The main loop
while(1 == 1):

    print("Please select the action from the following list you wish to perform by entering the number to its left")
    leosLib.printList(main_actions_list, True, 1)
    while(validIn == False):
        usrIn = input("> ")
        if(leosLib.intable(usrIn) == True):
            if(int(usrIn) > len(main_actions_list) or int(usrIn) < 1):
                validIn = False
                print("That input was not a number")
            else:
                validIn = True
        else:
            print("That input was not a number")

    if(float(usrIn) == 1):
        targetRow = findFirstEmpty(3)
        targetRowTwo = findFirstEmptyTwo(3)
        transactionId = findFirstEmpty(15)
        transactionId -= 1

        print("You have selected the buy an item option, this requires you to first enter the name of the item")
        item = input("> ")

        print("Now please enter the amount of the item you purchased, make sure you enter it correctly, you will not be repromted")
        amount = input("> ")

        print("Now please enter the total TT value of the item(s) purchased, once again make sure its entered correctly")
        print("If the tt value is very low, like for blazars for example, just enter 0 for the tt value if its less than a pec")
        ttValue = input("> ")

        print("Now please enter the total paid price of the item(s) purchased in ped, once again make sure its entered correctly")
        paidTotal = input("> ")

        # This part writes to the transaction sheet at the target row in the buy section
        fillCell(targetRow, 3, transactionId)

        fillCell(targetRow, 4, item)

        fillCell(targetRow, 5, amount)

        fillCell(targetRow, 6, paidTotal)

        fillCell(targetRow, 7, ttValue)

        # This part writes to the Inventory sheet at the inventory target

        fillCellTwo(targetRowTwo, 3, item)

        fillCellTwo(targetRowTwo, 4, amount)

        fillCellTwo(targetRowTwo, 5, ttValue)

        fillCellTwo(targetRowTwo, 6, paidTotal)



        # This part writes to the transaction sheet at the target row in the transaction history section

        fillCell(transactionId + 1, 15, transactionId)

        fillCell(transactionId + 1, 16, item)

        fillCell(transactionId + 1, 17, amount)

        fillCell(transactionId + 1, 18, paidTotal)

        fillCell(transactionId + 1, 19, ttValue)

        fillCell(transactionId + 1, 20, "Buy")

        transactionWorkbook.save("transaction-history.xlsx")

        print("Your purchase of " + item + " has been added to the transaction log, here is the transaction summary:")
        print("Transaction ID: " + str(transactionId))
        print("Item: \t" + item)
        print("Amount: \t" + amount)
        print("TT value: \t" + ttValue + " Ped")
        print("Ped paid: \t" + paidTotal + " Ped")

    elif(int(usrIn) == 2):
        inventoryItemList = []
        inventoryItemAmount = []
        inventoryItemValue = []
        inventoryItemPaidPed = []
        combinedList = []
        tempString = ""
        rowTotal = findFirstEmptyTwo(3)

        # This reads all the item names in the inventory sheet and adds them to a list
        for x in range(2, rowTotal):
            inventoryItemList.append(readCellTwo(x, 3))

        # This reads all the amounts in the inventory sheet and adds them to a list
        for x in range(2, rowTotal):
            inventoryItemAmount.append(readCellTwo(x, 4))

        #This reads all the TT values of the items and adds them to a list
        for x in range(2, rowTotal):
            inventoryItemValue.append(readCellTwo(x, 5))

        #This reads all the paid amounts of the items and adds them to a list
        for x in range(2, rowTotal):
            inventoryItemPaidPed.append(readCellTwo(x, 6))

        #This takes some of the item info and combines it into a list to be printed to the user
        for x in range(len(inventoryItemList)):
            tempString = "| Item: " + inventoryItemList[x] + "; Amount: " + inventoryItemAmount[x] + ";"
            combinedList.append(tempString)

        print("You have selected the sell option, next you will be showed a summary list of items in the inventory, hit enter to continue")
        input()

        chosenItem = 0
        sellAmount = 0
        sellPed = 0
        loop = True
        while(loop == True):
            print("To select an item type to see aditional information on it and to continue the transaction enter the number to its left")
            leosLib.printList(combinedList, True, 1)
            usrIn = ""

            while(usrIn == ""):
                usrIn = input("> ")
                if(leosLib.intable(usrIn) == True):
                    usrIn = int(usrIn)
                    if(usrIn > len(inventoryItemList) or usrIn < 0):
                        usrIn = ""
                        print("That selection was an invalid range")
                else:
                    usrIn = ""

            print("You have selected " + inventoryItemList[usrIn - 1] + " here is the entry's information")
            print("Amount: " + inventoryItemAmount[usrIn - 1])
            print("Total TT value: " + inventoryItemValue[usrIn - 1] + " Ped")
            print("Paid price: " + inventoryItemPaidPed[usrIn - 1] + " Ped")
            if(float(inventoryItemAmount[usrIn - 1]) > 1):
                markUp = float(inventoryItemPaidPed[usrIn - 1]) - float(inventoryItemValue[usrIn - 1])
                markUp = markUp / float(inventoryItemValue[usrIn - 1])
                markUp *= 100.0
                markUp += 100.0
                markUp = str(markUp)
                print("Effective markup: " + markUp + "%")
            else:
                markUp = float(inventoryItemPaidPed[usrIn - 1]) - float(inventoryItemValue[usrIn - 1])
                markUp = str(markUp)
                print("Effective markup: " + markUp + " Ped\n")

            chosenItem = usrIn -1

            usrIn = " "

            print("If you would like to continue to sell the selected item or a certain amount of it hit enter or to go back to the inventory list enter E")
            while(usrIn == " "):
                usrIn = input("> ")
                if(usrIn.lower() == "e"):
                    break
                elif(usrIn.lower() == ""):
                    loop = False
                else:
                    usrIn = " "
                    print("That input was not valid, try again")

        print("You will now be prompted to fill in some information for the sale")
        usrIn = ""
        if(float(inventoryItemAmount[chosenItem]) > 1):
            print("Firstly how much of the item do you want to sell ?")
            while(usrIn == ""):
                usrIn = input("> ")
                if(leosLib.intable(usrIn) ==True):
                    if(float(usrIn) < 1 or float(usrIn) > float(inventoryItemAmount[chosenItem])):
                        usrIn = ""
                        print("The chosen amount was not valid, as a reminder there are " + inventoryItemAmount[chosenItem] + " of that item")
                else:
                    print("The entered value was not valid")
                    usrIn = ""
            sellAmount = int(usrIn)
        else:
            print("There is only one of the item to sell so no need to enter an amount")

        usrIn = ""
        print("Now please enter the amount in ped you are selling the item(s) for ")
        while(usrIn == ""):
            usrIn = input("> ")
            if(leosLib.intable(usrIn) == True):
                if(float(usrIn) < 0):
                    print("The entered value was not valid")
                    usrIn = ""
        sellPed = float(usrIn)

        ttSoldValue = 0
        ttSoldValue = float(inventoryItemValue[chosenItem]) / float(inventoryItemAmount[chosenItem])
        ttSoldValue *= float(sellAmount)

        paidValueLeftOver = 0
        paidValueLeftOver = float(inventoryItemPaidPed[chosenItem]) / float(inventoryItemAmount[chosenItem])
        paidValueLeftOver *= float(sellAmount)
        paidValueLeftOver = float(inventoryItemPaidPed[chosenItem]) - paidValueLeftOver

        print("Thank you, please wait while the entry is added to the spreadsheet")

        targetRow = findFirstEmpty(3)
        targetRowTwo = findFirstEmptyTwo(3)
        transactionId = findFirstEmpty(15)
        transactionId -= 1

        print("Filling out transaction sheet (1/2)")

        # This part writes to the transaction sheet at the target row in the sell section
        fillCell(targetRow, 9, transactionId)

        fillCell(targetRow, 10, inventoryItemList[chosenItem])

        fillCell(targetRow, 11, sellAmount)

        fillCell(targetRow, 12, round(sellPed), 2)

        fillCell(targetRow, 13, round(ttSoldValue), 2)

        print("Filled out transaction sheet (1/2)")


        print("Filling out Inventory sheet (1/1)")
        # This part writes to the Inventory sheet at the item being sold

        if(int(inventoryItemAmount[chosenItem]) - sellAmount > 0):
            fillCellTwo(chosenItem + 2, 3, inventoryItemList[chosenItem])

            fillCellTwo(chosenItem + 2, 4, int(inventoryItemAmount[chosenItem]) - sellAmount)

            fillCellTwo(chosenItem + 2, 5, round(float(inventoryItemValue[chosenItem]) - ttSoldValue, 2))

            fillCellTwo(chosenItem + 2, 6, round(paidValueLeftOver, 2))

            print("Filled out Inventory sheet (1/1)")

        else:
            fillCellTwo(chosenItem + 2, 3, None)

            fillCellTwo(chosenItem + 2, 4, None)

            fillCellTwo(chosenItem + 2, 5, None)

            fillCellTwo(chosenItem + 2, 6, None)

            print("Filled out Inventory sheet (1/1)")

            print("Reorganizing Inventory sheet (1/1)")
            reorganizeBalance()
            print("Reorganized Inventory sheet (1/1)")



        # This part writes to the transaction sheet at the target row in the transaction history section

        print("Filling out transaction sheet (2/2)")

        fillCell(transactionId + 1, 15, transactionId)

        fillCell(transactionId + 1, 16, inventoryItemList[chosenItem])

        fillCell(transactionId + 1, 17, sellAmount)

        fillCell(transactionId + 1, 18, round(sellPed, 2))

        fillCell(transactionId + 1, 19, round(ttSoldValue, 2))

        fillCell(transactionId + 1, 20, "Sell")

        transactionWorkbook.save("transaction-history.xlsx")

        print("Filled out transaction sheet (2/2)")

        print("Transaction succesfully documented")

    break