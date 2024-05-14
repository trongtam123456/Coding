# y tuong la cat doi thanh 2 phan, 1 phan nho va 1 phan lon roi xep xen ke
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr1 = arr[:int(len(arr)/2)]
arr2 = arr[int(len(arr)/2):]
#print(arr1)
#print(arr2)
list_new = []
if len(arr1) == len(arr2):
    for i in range(0, len(arr1)):
        list_new.append(arr2[i])
        list_new.append(arr1[i])
else:
    nganhon = min(len(arr1), len(arr2))
    for k in range(nganhon):
        list_new.append(arr2[k])
        list_new.append(arr1[k])
    if len(arr1) > len(arr2):
        list_new.append(arr1[nganhon])
    else:
        list_new.append(arr2[nganhon])

# xu ly chinh so luong hang re
soluong = 0
for m in range(1, len(list_new)-1):
    if list_new[m] < list_new[m-1] and list_new[m] < list_new[m+1]:
        soluong = soluong + 1

print(soluong)
