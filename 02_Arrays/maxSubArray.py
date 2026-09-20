# Given an array 'nums'. Find the sub array with largest sum and return the sum
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6 ; sub Array [4,-1,2,1] has the maximum sum 6.


#                                   BRUTE FORCE APPROACH
# CALCULATE THE SUM OF EACH POSSIBLE SUBARRAY AND RETURN THE MAXIMUM SUM
def maxSubArray(nums):
    n = len(nums)
    max_sum = -10 ** 18         # Least possible value available
    for i in range(n):
        for j in range(i,n):
            sm = 0
            for x in range(i, j+1):
                sm += nums[x]
            max_sum = max(max_sum,sm)
    return max_sum





#                               BETTER APPROACH
# Use only two loop to store and update the sum.
def maxSubArray(nums):
    n = len(nums)
    max_sum = -10 ** 18
    for i in range(n):
        sm = 0
        for j in range(i,n):
            sm += nums[j]
            max_sum = max(max_sum,sm)
    return max_sum




#                           OPTIMAL APPROACH
#                          KADANE'S ALGORITHM
def maxSubArray(nums):
    n = len(nums)
    max_sum = -10 ** 18
    sm = 0
    for i in range(n):
        sm += nums[i]
        max_sum = max(max_sum,sm)
        
        if sm < 0:
            sm = 0
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))




#              Few changes in the KADANE'S ALGORITHM code if queston asked to return the SubaArray as well
def maxSubArray(nums):
    n = len(nums)
    max_sum = -10 ** 18
    sm = 0
    arr_start = -1
    arr_end = -1
    for i in range(n):
        if sm == 0:
            start = i
        sm += nums[i]

        if sm > max_sum:
            max_sum = sm
            arr_start = start
            arr_end = i
        if sm < 0:
            sm = 0
    return max_sum , nums[arr_start : arr_end+1]

nums = [-2,1,-3,4,-1,2,1,-5,4]
max_sum , SubArray = maxSubArray(nums)
print(f"max_sum :{max_sum}")
print(f"Sub_Array :{SubArray}")