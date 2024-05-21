low = int(input())
hight = int(input())
dem = 0
lisst = []
for i in range(low, hight + 1):
    if (i%2!=0):
        dem += 1
        lisst.append(i)
print('so luong so le la ', dem)
print('The odd numbers between',low,'and',hight,'are',lisst)