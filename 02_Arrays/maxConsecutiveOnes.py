# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# input: nums = [0,1,1,0,1,1,1,0,1]
# output:  3

def maxCosecutiveOnes(nums):
    n = len(nums)
    count = 0
    max_i = 0
    for i in range(n):
        if nums[i] == 1:
            count += 1
            max_i = max(max_i, count)
        else:
            count =0
    return max_i