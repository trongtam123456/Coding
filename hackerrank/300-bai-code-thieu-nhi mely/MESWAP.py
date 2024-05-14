#nhap mang a va b 
n = int(input())
nho = list(map(int , input().split()))
lon = list(map(int , input().split()))
def sapxep():
    for i in range(0, n):
        if lon[i] > nho[i]:
            continue
        else:
            tmp = nho[i]
            nho[i] = lon[i]
            lon[i] = tmp
sapxep()
print(max(lon) * max(nho))