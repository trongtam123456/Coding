def check(lst, k):
    for idx, price in enumerate(lst):
        if price <= k and price != 0:
            return idx + 1  
    return -1

n, m, k = map(int, input().split())
arr_tro = list(map(int, input().split()))


vitri = m - 1

list1 = arr_tro[:vitri][::-1] 
list2 = arr_tro[vitri + 1:]  


result1 = check(list1, k)
result2 = check(list2, k)


if result1 != -1:
    result1 = (result1) * 10 
if result2 != -1:
    result2 = (result2) * 10  


if result1 == -1 and result2 == -1:
    print("-1")
elif result1 != -1 and (result2 == -1 or result1 <= result2):
    print(result1)
else:
    print(result2)
