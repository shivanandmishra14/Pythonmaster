menu = [
    ["egg", "beacon"],
    ["egg", "bread", "spam"]
]

for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)

    else:
        print("{0} has a spam score of {1}".format(meal, meal.count("spam")))