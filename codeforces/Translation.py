strings1 = input()
strings2 = input()
dao = ""

# Reverse strings2
for i in range(len(strings2) - 1, -1, -1):
    dao = dao + strings2[i]

# Check if the reversed string matches strings1
if dao == strings1:
    print("YES")
else:
    print("NO")
