n = int(input())
lst_result = []
for i in range(0, n):
    le_lon_nhat = 1
    number = int(input())
    if number%2!=0:
        lst_result.append(number)
    else:
        for k in range(1, number):
            if number%k == 0 and k%2 != 0:
                le_lon_nhat = k
        lst_result.append(le_lon_nhat) 
for j in lst_result:
    print(j)