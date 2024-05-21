def kiemtra(nums):
    chenhlech = nums[0][1] - nums[0][0]
    for k in range(1, len(nums)):
        chenhlech1 = nums[k][1] - nums[k][0]
        if chenhlech1 != chenhlech:
            return False
    return True 

nums = [[5, 7], [6, 8], [3, 5], [9, 11]]
if len(nums) == 1:
    print('day la diem khong phai doan thang')
elif len(nums) == 2:
    print('day la', len(nums), 'diem thang hang')
else:
    print(kiemtra(nums))

