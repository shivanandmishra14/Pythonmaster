name = input("name: ")
age = int(input("age {0}" . format(name)))
print(age)

if age >= 18:
    print("you are eligible for voting")
else:
    print("please comeback in {0} years". format(18-age))

# otherway
if age < 18:
    print("please comeback in {0} years".format(18 - age))
else:
    print("you are eligible for voting")
    print("please put an X in the box ")
