#https://codeforces.com/problemset/problem/155/A
n = int(input())
list = input().split()
list_new= []
for i in list:
    list_new.append(int(i))
#print(list_new)
min = list_new[0]
max = list_new[0]
dem = 0
for i in list_new:
    #check min
    if i > max:
        max = i
        dem = dem + 1
    elif i < min:
        min = i
        dem = dem + 1
print(dem)
