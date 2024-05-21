strings = input()
new_str = ''
for i in range(0, len(strings)):
    new_str = new_str + strings[i].lower()
print(new_str)