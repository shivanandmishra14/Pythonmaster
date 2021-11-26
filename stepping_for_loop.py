number = "9,223;4320:444; 854,775;805"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators+char
print(separators)