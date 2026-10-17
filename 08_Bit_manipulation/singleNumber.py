#                               136. Single Number
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example :
Input: nums = [2,2,1]
Output: 1

"""

def singleNumber(nums):
    ans = 0
    for i in range(len(nums)):
        ans = ans ^ nums[i]
    return ans


nums = [1,2,3,2,3,5,5]
print(singleNumber(nums))