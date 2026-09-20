# ASCENDING ORDER SORTING
# input: nums = [5,2,3,1]

nums = [9,8,7,6]
def insertion_sort(nums):
    n = len(nums)
    for i in range(1,n):
        key  = nums[i]
        j = i-1
        while j>=0 and nums[j]>key:
            nums[j+1] = nums[j]
            nums[j] = key
            j = j-1

    return nums

print(insertion_sort(nums))
