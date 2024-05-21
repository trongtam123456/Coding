arr = [[3, 5, 8, 9, 10], 
       [3, 4, 7, 9, 30], 
       [4, 5, 6, 3, 40], 
       [6, 7, 9, 3, 16],
       [1, 6, 8, 4, 50]]
sum1 = 0
sum2 = 0
for i in range(0, len(arr)):
#tong duong cheo chinh
    sum1 = sum1 + arr[i][i]
#tong duong cheo phu
h = len(arr)
j = 0
for i in range(0, len(arr)):
    sum2 = sum2 + arr[h-1][j]
    h = h-1
    j = j+1
print(sum1 + sum2)

