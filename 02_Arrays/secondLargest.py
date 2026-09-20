#Input: nums= [1,2,2,3,5,6]
# output: 5 ; it's the second largest number present in the array``
def secondLargest(nums):
    n = len(nums)
    largest = nums[0]
    second_largest = -1
    for i in range(n):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        else:
            if nums[i]< largest and nums[i]> second_largest:
                second_largest = nums[i]
    return second_largest

nums = [8, 8, 7, 6, 5]    
print(secondLargest(nums))
