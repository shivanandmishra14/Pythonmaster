choice = ""
while choice != "0":
    if choice in "1234":
        print("you choose {}".format(choice))
    else:
        print("1. \t Learn python")
        print("2. \t Learn java")
        print("3. \t Learn JS")
        print("4. \t Learn HTML")

    choice = input()