nums = [6, 4, 3, 0, 2, 5, 0, 9]
for i in range(len(nums)):
    if (nums[i] == 0):
        nums.remove(0)
        nums.append(0)
print(nums)