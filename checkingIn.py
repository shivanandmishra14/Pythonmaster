parrot = "Norweign blue"
letter = input("ENter a charatcter :")
if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("Dont need that character")


activity = input(" WHat would you like to do it today: ")
if "cinema" not in activity:
    print("But I want to go")