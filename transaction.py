import openpyxl
import leosLib


# Here is where all the necessary excel documents are opened
transactionWorkbook = openpyxl.load_workbook("transaction-history.xlsx")
transactionSheet = transactionWorkbook.active
current_cell = transactionSheet.cell(row = 100, column = 100)

def findFirstEmpty(checkedCollum):
    currentRow = 1
    current_cell = transactionSheet.cell(row=1, column=checkedCollum)
    while(current_cell.value != None):
        currentRow += 1
        current_cell = transactionSheet.cell(row = currentRow, column = checkedCollum)
    return currentRow


validIn = False
usrIn = ""
main_actions_list = ["Buy an item (add it to the stock database)",
                     "Sell an item (remove it from the stock database)",
                     "Edit an entry of an item in the stock database (this is for if items are removed without being sold or if you entered a value wrong/need to edit TT or paid value of an entry"]

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

        # This part writes to the sheet at the target row in the buy section
        current_cell = transactionSheet.cell(row=targetRow, column=3)
        current_cell.value = str(transactionId)

        current_cell = transactionSheet.cell(row=targetRow, column=4)
        current_cell.value = item

        current_cell = transactionSheet.cell(row=targetRow, column=5)
        current_cell.value = amount

        current_cell = transactionSheet.cell(row=targetRow, column=6)
        current_cell.value = paidTotal

        current_cell = transactionSheet.cell(row=targetRow, column=7)
        current_cell.value = ttValue

        # This part writes to the sheet at the target row in the transaction history section
        current_cell = transactionSheet.cell(row=transactionId + 1, column=15)
        current_cell.value = str(transactionId)

        current_cell = transactionSheet.cell(row=transactionId + 1, column=16)
        current_cell.value = item

        current_cell = transactionSheet.cell(row=transactionId + 1, column=17)
        current_cell.value = amount

        current_cell = transactionSheet.cell(row=transactionId + 1, column=18)
        current_cell.value = paidTotal

        current_cell = transactionSheet.cell(row=transactionId + 1, column=19)
        current_cell.value = ttValue

        current_cell = transactionSheet.cell(row=transactionId + 1, column=20)
        current_cell.value = "Buy"

        transactionWorkbook.save("transaction-history.xlsx")

        print("Your purchase of " + item + " has been added to the transaction log, here is the transaction summary:")
        print("Transaction ID: " + str(transactionId))
        print("Item: \t" + item)
        print("Amount: \t" + amount)
        print("TT value: \t" + ttValue + " Ped")
        print("Ped paid: \t" + paidTotal + " Ped")
    break