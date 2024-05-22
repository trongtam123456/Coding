def nguyento(k):
    if k < 2:
        return False
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True

n = int(input())
list = []
for i in range(2, n + 1):
    if nguyento(i):
        list.append(i)
# in 
for i in list:
    print(i, end =' ')
