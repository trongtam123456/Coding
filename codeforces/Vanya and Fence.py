# Nguồn : https://codeforces.com/problemset/problem/677/A
n, height = map(int, input().split())
list = []
strings = input()
list = strings.split()
dem = 0
for i in list:
    if height<int(i):
        dem = dem + 2
    else:
        dem = dem + 1
print(dem)