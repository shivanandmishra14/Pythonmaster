data = [4, 5, 105, 110, 120, 130, 130, 150, 160, 170, 183,
        185, 187, 188, 191, 350, 360]

min_value = 100
max_value = 200

start = 0
for index in range(len(data) - 1, -1, -1):
    # print(index)
    if data[index] <= max_value:
        start = index + 1
        break

print(start)
del data[start:]
print(data)