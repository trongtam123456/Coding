num1 = [2, 4, 6]
num2 = [5, 3, 5]
#dao nguoc
num1_new = ""
num2_new = ""
for i in range(len(num1)-1, -1, -1):
    num1_new = num1_new + str(num1[i])
for i in range(len(num2)-1, -1, -1):
    num2_new = num2_new + str(num2[i])
# chuyen ve int 
num1_new = int(num1_new)
num2_new = int(num2_new)
tich = num1_new*num2_new
list_tich = [int(i) for i in str(tich)[::-1]]
print(list_tich)