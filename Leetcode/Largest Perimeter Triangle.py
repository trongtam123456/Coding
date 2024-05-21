nums = [3, 6, 7, 8, 9, 3, 6, 2, 6, 4]
nums = sorted(nums)
for i in range(1, len(nums)-2):
    #kiem tra tam giac
    a = nums[-i]
    b = nums[-i-1]
    c = nums[-i-2]
    print(a, b, c)
    if (a**2 + b**2 > c**2) and (a**2 + c**2 > b**2) and (b**2 + c**2 > a**2):
        print('tam giac co chu vi lon nhat la ', a+b+c,'co canh lan luot la', a, b, c)
        break