#Input: nums= [1,2,2,3,5,6]
# output: 6 ; it's the largest number present in the array
def largestElement(nums):
    n = len(nums)
    largest = nums[0]
    for i in range(n):
        if nums[i] > largest:
            largest = nums[i]
        i += 1
    return largest

nums = [2,3,4,1,9,4,7,0]
print(largestElement(nums))




