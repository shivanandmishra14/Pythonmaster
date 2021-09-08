import re

#  By using count method
string = "abcdabcdefab"
count = string.count("a")
print(count)

# ==================
#  Without using count method
new_String = "abcdabcdefab"
print(len(re.findall("a", new_String)))

# =============================
