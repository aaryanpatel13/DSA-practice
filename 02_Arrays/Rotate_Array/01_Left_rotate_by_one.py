def leftRotate(nums):
    n = len(nums)
    temp = nums[0]
    for i in range(1,n):
        nums[i-1] = nums[i]
        i += 1
    nums[n-1] = temp

    return nums

#Example
nums = [1,2,3,4,5]
rotate = leftRotate(nums)
print(rotate)