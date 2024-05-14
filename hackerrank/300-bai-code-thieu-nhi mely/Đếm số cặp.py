n, x = map(int, input().split())
arr = list(map(int, input().split()))
cap = 0
# lay 1 so tu mang
for i in range(0, len(arr)):
    so_1 = arr[i]
    if i<=len(arr):
        arr_new = arr[i:]
        for k in range(0, len(arr_new)):
            so_2 = arr_new[k]
            if so_1*so_1 + so_2 == x:
                cap = cap + 1
print(cap)