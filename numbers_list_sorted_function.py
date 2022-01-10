pangram = "The quick brown fox jumps over a lazy dog"
letters = sorted(pangram)
print(letters)

#  Sort numbers
numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6, 7]
sorted_num = sorted(numbers)
print(sorted_num)


# What is the difference between sort and sorted
numbers.sort()
print(numbers)

#  Here the output is same but Sorted gives a new list and sort modifys the exisitng list

# Try sort to store in new variable
sort_another_number = numbers.sort()
print(sort_another_number)


