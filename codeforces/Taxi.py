group = int(input())
list = list(map(int, input().split()))
#print(list)
sum = 0
for i in list:
    sum = sum + i

if sum%4!=0:
    print(sum//4+1)
else:
    print(sum//4)