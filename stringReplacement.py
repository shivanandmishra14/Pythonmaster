age = 28
print("My age is " + str(age) + " years")

#  Use format to pass value
print("My age is {0} years ".format(age))

# Multiple replacements by using format
print(" {0} is the  age of my  friends who all are "
      "{1}, {2}, {3}, {4}, {5}".format(28, "Rahul", "suresh",
                                       "Nitin", "parul", "nayan"))

print("Rahul: {0}, Parul: {1}, Nayan: {2}, Arti: {3}, Jaya: {4}, Sindhu: {5}"
      .format(28, 29, 30, 31, 27, 34))

print("""Rahul: {0}, 
Parul: {1}, 
Nayan: {2}, 
Arti: {3}, 
Jaya: {4},
Sindhu: {5}"""
      .format(28, 29, 30, 31, 27, 34))

