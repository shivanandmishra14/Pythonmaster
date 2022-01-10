pangram = sorted("The quick brown fox jumps over a lazy dog", key=str.casefold)
print(pangram)


#  try with sort method
names = ["Graham", "John", "terry", "eric", "Terry", "Michael"]
names.sort(key=str.casefold)
print(names)
