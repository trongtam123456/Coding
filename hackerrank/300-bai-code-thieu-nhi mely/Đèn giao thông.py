def timkhoangcachlonnhat(den):
    khoangcach = []
    for k in range(1, len(den)):
        khoangcach.append(int(den[k])- int(den[k-1]))
    return max(khoangcach)


lst_result = []
den_add = []
x, n = map(int, input().split())
lst = list(map(int, input().split()))
den_add.append(x)
for i in lst:
    den_add.append(i)
    den_add.sort()
    lst_result.append(timkhoangcachlonnhat(den_add))
for index in lst_result:
    print(index, end = ' ')