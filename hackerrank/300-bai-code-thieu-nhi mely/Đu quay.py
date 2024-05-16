def soluongtoithieu(arr, n, x):
    seat = 0
    # tao con tro ben trai - nhe nhat 
    i = 0
    # tao con tro ben phai - nang nhat
    j = n - 1
    while i<=j:
        # ghep nang nhat va nhe nhat voi nhau xem co hop le khong 
        if arr[i] + arr[j] <= x:
            i = i+1 # tang con tro cho i len 1 
        #neu khong hop thi nang nhat phai ngoi 1 minh
        j = j -1
        seat = seat + 1 
    return seat

n, x = map(int, input().split())
arr = list(map(int, input().split()))
# sap xep danh sach
arr.sort()
print(soluongtoithieu(arr, n, x))