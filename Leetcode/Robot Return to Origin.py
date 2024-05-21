"""Thuật toán: - Cho người dùng nhập bước vào, triệt tiêu L(trái) với R(phải) và D(lui) với U(tiến)"""
print('robot dang o vi tri (0, 0), vui long chon buoc di: ',end = '' )
buoc = input()
#dem so luong D U L R
so_D = 0
so_U = 0
so_R = 0
so_L = 0
buoc_new = ""
for i in range(0, len(buoc)):
    if (buoc[i] == "D"):
        so_D = so_D + 1
    elif (buoc[i] == "U"):
        so_U = so_U + 1
    elif (buoc[i] == "R"):
        so_R = so_R + 1
    elif (buoc[i] == "L"):
        so_L = so_L + 1
# xu ly buoc di
if (so_D < so_U):
    so_U = so_U - so_D
    buoc_new = buoc_new + so_U*"U"
elif (so_D > so_U):
    so_D = so_D - so_U
    buoc_new = buoc_new + so_D*"D"
if (so_L < so_R):
    so_R = so_R - so_L
    buoc_new = buoc_new + so_R*"R"
elif (so_L > so_R):
    so_L = so_L - so_R
    buoc_new = buoc_new + so_L*"L"
# ket qua 
if (buoc_new == ""):
    print("Robot tro ve cho cu")
else: 
    print("Robot khong tro ve vi tri cu")