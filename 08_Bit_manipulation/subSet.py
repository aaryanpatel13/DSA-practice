#                           78. Subsets   Using bit manipulation
"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

"""

def subset(nums):
    n = len(nums)
    t_sbset = 2 ** n
    res = []
    for num in range(t_sbset):
        ans = []
        for i in range(n):
            if num & (1 << i) != 0:
                ans.append(nums[i])
        res.append(ans)
    return res


nums = [1,2,3]
print(subset(nums))
