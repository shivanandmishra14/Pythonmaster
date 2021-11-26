for i in range(1, 20):
    print("i value {}".format(i))
print("===========================")


# If you don't provide the value it will take default as zero
for i in range(21):
    print("i value {}".format(i))
print("===========================")

#  skips 2 digits
for i in range(0, 20, 2):
    print("i value {}".format(i))
print("===========================")


# TO iterate from backwards like slicing
for i in range(20, 0, -2):
    print("i value {}".format(i))
print("===========================")


# now the operator we have used we have to use in range
age = int(input("HOw old are you? :"))
if age in range(16, 60):
    print("enjoy the time")
else:
    print("Have sometime to enjoy")