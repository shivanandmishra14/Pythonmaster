shopping_list = ["apple", "spam", "jira", "orange"]

item_to_find = "spam"
fond_at = None

# for index in range():
# Break we use to come out of loop
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        fond_at = index
        break

print("Item found at {}".format(fond_at))

# ======================================