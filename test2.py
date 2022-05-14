strings = ["a", "ab", "aa", "c"]
new_strings = []
for string in strings:
   new_string = string.replace("a", "1") 
   new_strings.append(new_string)
   print(new_strings)