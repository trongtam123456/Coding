# Nguồn : https://codeforces.com/problemset/problem/1692/A
testcase = int(input())
list_result = []
for i in range(0, testcase):
    string = input()
    list_str = string.split()
    dem = 0
    #Check ket qua 
    for k in range(1, len(list_str)):
        if int(list_str[0]) < int(list_str[k]):
            dem = dem + 1
    list_result.append(dem)
# in ket qua 
for j in list_result:
    print(j)
