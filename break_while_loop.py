available_exit = {"north", "south", "east", "west"}
chosen_exit = ""

while chosen_exit not in available_exit:
    chosen_exit = input("please choose the direction :")
    # if chosen_exit == "upsides" :
    if chosen_exit.casefold() == "upsides" :
        print("game over")
        break

print("aren't you glad out there")