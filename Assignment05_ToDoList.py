# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog:    REV_0
#               Fernando Hernandez
#               11/09/19
#               Added code to complete assignment 5 which consists of loading Data into
#               a txt.file dictionary and then to a list table. Work will be posted to "GitHub".
# ------------------------------------------------------------------------ #

# -- Declaring Variables -- #

strFile = "ToDoList.txt"
objFile = None
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Displaying Menu -- #

while (True):
    print("""
    Menu of Options 
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)

# -- Loading Initial Data from ToDoList.txt -- #

    objFile = open(strFile, "r")
    for row in objFile:
        lstRow = row.split(",")
        dicRow = {lstRow[0].strip()}
    objFile.close()
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

#  -- Showing Current Data -- #

    if (strChoice.strip() == '1'):
        print(dicRow)
        for row in lstTable:
            print(row)
        continue

#  -- Adding New Items to Table -- #

    elif (strChoice.strip() == '2'):
        strItem = (input("\n" + "Please, add a Task to perform -->  "))
        strValue = (input("\n" + "Thanks, now enter its Priority Number -->  "))
        dicRowNew = {"Task":strItem, "Priority#":strValue}
        lstTable.append(dicRowNew)
        print("\n" + "Thank you, data has been added! " + "\n")
        continue

# -- Removing items from List -- #

    elif (strChoice.strip() == '3'):
        strItem = input("\n" + "Please, tell me which Task you want to remove -->  ")
        for row in lstTable:
            if strItem in row:
                del row[strItem]
        else:
            print()
            print(strItem, "Not in the List")
        continue

# -- Saving tasks to the ToDoToDoList.txt file -- #

    elif (strChoice.strip() == '4'):
        with open('ToDoList.txt', 'a') as filehandle:
            for listitem in lstTable:
                    filehandle.write('%s\n' % listitem)
        print("\n" + "Great!, ... Your data has been saved.")

# -- Exiting Program -- #

    elif (strChoice.strip() == '5'):
        print("Bye, Bye!!!")
        break