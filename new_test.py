str1 = "abcdef"
str2 = "defghia"
c, j = 0, 0
for i in str1:
    if str2.find(i) >= 0 and j == str1.find(i):
        c += 1
    j += 1
print('No. of matching characters are : ', c)