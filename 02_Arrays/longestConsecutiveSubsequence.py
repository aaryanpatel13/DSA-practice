"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

"""

#                                           BRUTE FORCE APPROACH
#                                           Time Complexti: O(N²)
#                                           Space Complexity: O(1)
def longestConsecutive(nums):
    max_cnt = 0
    for i in range(len(nums)):
        num = nums[i]
        count = 1
        while num+1 in nums:
            count += 1
            num  = num+1
        max_cnt = max(max_cnt,count)
    return max_cnt

nums = [1,0,1,2]
print(longestConsecutive(nums))



#                                           BETTER APPROACH
#                                           Time Complexti: O(NlogN + N)
#                                           Space Complexity: O(1)


def longestConsecutive(nums):
    nums.sort()
    n = len(nums)
    prev_ele = -10 ** 18
    count = 0
    longest = 0
    for i in range(n):
        if nums[i]-1 == prev_ele:
            count += 1
            prev_ele = nums[i]
        elif nums[i] == prev_ele:
            continue
        else:
            count= 1
            prev_ele = nums[i]
        
        longest = max(count,longest)
    return longest


nums = [1,0,1,2]
print(longestConsecutive(nums))

#                                           OPTIMAL APPROACH
#                                           Time Complexti: O(N)
#                                           Space Complexity: O(N)


def longestConsecutive(nums):
    nums = set(nums)
    longest = 0
    for num in nums:
        if (num - 1) in nums: # this means current num se sequence ni start ho rha..issliye skip checking for this
            continue
        count = 1
        while num+1 in nums:
            count += 1
            num = num+1
        longest = max(count,longest)
    return longest 

nums = [1,0,1,2]
print(longestConsecutive(nums))