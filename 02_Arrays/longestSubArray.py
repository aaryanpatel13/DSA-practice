# Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to 'K'. 
# If no such sub-array exists, return 0.
# The array contains only POSITIVE numbers.
# Input: nums = [10,5,2,7,1,9], k = 15
# Output: 4 ; sub-array = [5,2,7,1] is of len = 4


#                                   BRUTE FORCE APPROACH
def longestSubArray(nums,k):
    n = len(nums)
    longest = 0
    for i in range(n):
        for j in range(i,n):
            sm = 0
            for x in range(i,j+1):
                sm += nums[x]
            if sm == k:
                longest = max(longest, (j-i)+1)
    return longest




#                                 BETTER APPROACH [HASHING]
#                              WE ARE USING PREFIX SUM METHOD 
def longestSubArray(nums,k):
    n =len(nums)
    longest = 0
    prefix_sum_map = {}
    curernt_sum = 0
    
    for i in range(n):
        curernt_sum += nums[i]

        #If sub array indx is from 0 to i
        if curernt_sum == k:
            longest = max(longest, i+1)

        # If subarray is in the mid somewhere
        rem = curernt_sum - k
        if rem in prefix_sum_map:
            length = i - prefix_sum_map[rem]
            longest = max(longest, length)

        #If current_sum is not present in the map...store it there with its indx
        if curernt_sum not in prefix_sum_map:
            prefix_sum_map[curernt_sum] = i

    return longest

        
#                                   OPTIMAL APPROACH 

#                               SLIDING WINDOW APPROACH
# Sliding window is a TWO POINTERS APPROACH which can only be used when the array contains only POSITVE integers.

def longestSubArray(nums,k):
    n = len(nums)
    left = 0
    right = 0
    sm = 0
    max_len = 0
    for right in range(n):
        sm += nums[right]
        while left <= right and sm > k:
            sm -= nums[left]
            left +=1
        if sm == k:
            max_len = max(max_len, right - left +1)
    return max_len



# EXAMPLE``
nums = [0,1,1,2,3,1,0,1,1]
target = 3
print(longestSubArray(nums,target))