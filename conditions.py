# age = int(input("How old are you "))
#
# if age >= 16 and age <= 65:
#     print("have a great day")
# else:
#     print("enjoy free time")


# simplify the chained

age = int(input("How old are you "))
if 16 <= age <= 65:
    print("have a great day")
else:
    print("enjoy free time")

print("-" * 80)

# With or operator
if age < 16 or age > 65:
    print("have a great day")
else:
    print("enjoy free time")
