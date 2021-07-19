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
    current_cell.value = str(string)

def fillCellTwo(row, collum, string):
    current_cell = balanceSheet.cell(row=row, column=collum)
    current_cell.value = str(string)

def findFirstEmpty(checkedCollum):
    currentRow = 1
    current_cell = transactionSheet.cell(row=1, column=checkedCollum)
    while(current_cell.value != None):
        currentRow += 1
        current_cell = transactionSheet.cell(row = currentRow, column = checkedCollum)
    return currentRow

def findFirstEmptyTwo(checkedCollum):
    currentRow = 1
    current_cell = balanceSheet.cell(row=1, column=checkedCollum)
    while(current_cell.value != None):
        currentRow += 1
        current_cell = balanceSheet.cell(row = currentRow, column = checkedCollum)
    return currentRow


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

    if(int(usrIn) == 1):
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
    break