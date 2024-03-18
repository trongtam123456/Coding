#https://codeforces.com/problemset/problem/1676/A
n = int(input())
list_result = []
for i in range(0, n):
    a = input()
    sum_1 = int(a[0]) + int(a[1]) + int(a[2])
    sum_2 = int(a[3]) + int(a[4]) + int(a[5])
    if sum_1 == sum_2:
        list_result.append("YES")
    else:
        list_result.append("NO")
for i in list_result:
    print(i)
