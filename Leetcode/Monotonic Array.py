a = [7, 6, 5, 5, 9, 5, 5 ]
# xet diem dau va cuoi xem tang hay giam
if (a[0] > a[len(a)-1]):
    for i in range(1, len(a)):
        if (a[i] > a[i-1]):
            print('khong phai mang don dieu')
            break
        if (i == len(a)-1 and a[i] <= a[i-1]):
            print("day la mang don dieu")
elif (a[0] < a[len(a)-1]):
    for i in range(0, len(a)):
        if (a[i] < a[i-1]):
            print('khong phai mang don dieu')
            break
        if (i == len(a)-1 and a[i] >= a[i-1]):
            print("day la mang don dieu")

else:
    print("khong phai mang don dieu")
