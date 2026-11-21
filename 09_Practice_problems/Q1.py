#                                   Count Valid Subarrays of Size 3
"""Problem Description
You are given an array of integers containing N elements. Your task is to find and return an integer value representing the total number of subarrays of size 3 where the sum of the first element and the third element is equal to the second element.

A subarray is a continuous sequence of elements in an array.

Input Specification
Input 1: An integer array of size N.
Input 2: An integer value N, representing the size of the array.
Output Specification
Return an integer value representing the total number of subarrays of size 3 that satisfy the given condition.

Example:
Input: [1, 2, 1, 3, 5, 2, 4, 2], 8
Output: 3

"""
def validSub(nums):
    n = len(nums)
    count = 0
    for i in range(n-2):
        if (nums[i] + nums[i+2]) == nums[i+1]:
            count += 1
    return count


nums = [1, 2, 1, 3, 5, 2, 4, 2]
print(validSub(nums))