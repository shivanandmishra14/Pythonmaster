name = input("name: ")
age = int(input("age {0}".format(name)))
print(age)

if age < 18:
    print("please comeback in {0} years".format(18 - age))

elif age == 90:
    print("please take rest  vote whenever you want")

else:
    print("you are eligible for voting")
    print("please put an X in the box ")
