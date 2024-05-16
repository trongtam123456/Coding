n = int(input())
uoc = []
if n == 1:
    print("YES")
else:
    for i in range(1, n+1):
        if n%i==0:
            uoc.append(i)

# tinh
    tong = 0
    for k in uoc:
        tong =  tong + k
    if tong/2 == n:
        print("YES")
    else:
        print("NO")
