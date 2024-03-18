#https://codeforces.com/problemset/problem/266/A
n = int(input())
strings = input()
dem = 0
for i in range(1, len(strings)):
    if strings[i] == strings[i-1]:
        dem = dem + 1
print(dem)