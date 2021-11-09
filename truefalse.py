# day = "Monday"
# temperature = 30
# raining = True
#
# if day == "Saturday" and temperature > 27 and not raining:
#     print("Go swim")
# else:
#     print("Learn python")

# day == "Saturday" false condition, not raining is also false hence else block executed

# ========================================================================================

day = "Saturday"
temperature = 30
raining = True

if day == "Saturday" and temperature > 27 or not raining:
    print("Go swim")
else:
    print("Learn python")

# first condition day == "Saturday matched so if executed.
# and has precedence than or in python


# always use bracket for and and or usage in condition
# if (day == "Saturday" and temperature > 27) or not raining:
