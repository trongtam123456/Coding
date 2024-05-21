a = [1, 3, 7, 5, 11, 9]
#sap xep a tang dan
a = sorted(a)
dem = 1
#kiem tra co trung cong sai khong
for i in range(1, len(a) - 2):
    d = a[2] - a[0]
    if (d == a[i+2] - a[i]):
        dem =   dem + 1
if ( dem == len(a)-2 ):
    print("cap so cong")
else:
    print("dech phai cap so cong")