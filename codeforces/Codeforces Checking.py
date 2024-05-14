a = int(input())
result = []
for i in range(0, a):
    char = input()
    if char in "codeforces":
        result.append("YES")
    else: 
        result.append("NO")
for i in result:
    print(i)
