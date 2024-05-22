n = int(input())
lst = list(map(int, input().split()))
# sap xep
lst.sort()
#print(lst)
# tao bien lst2 la khoang cach
lst2 = []
for i in range(1, n):
    khoangcach = lst[i] - lst[i-1]
    lst2.append(khoangcach)
#print(lst2)
# in ket qua 
for item in range(0, len(lst2)):
    if min(lst2) == lst2[item]:
        print(str(lst[item]) + ' ' + str(lst[item+1]), end = ' ')

 

