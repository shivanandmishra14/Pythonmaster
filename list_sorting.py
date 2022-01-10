even = [1, 2, 3, 4, 5]
odd = [6, 7, 8, 9, 0]

even.extend(odd)
print(even)

even.sort()
print(even)

even.sort(reverse=True)
print(even)