"""
Given an array arr[] of non-negative integers and an integer target, count all subsets of the array whose sum is equal to the given target.
Example:
Input: nums = [5, 2, 3, 10, 6, 8], target = 10
Output: 3

"""

def perfectSum(nums,target):
    n = len(nums)
    res = []
    
    def validSubset(nums,subs,indx,total):
        if indx == n:
            if total == target:
                res.append(subs[:])
            return
        
        # pick element
        subs.append(nums[indx])
        total += nums[indx]
        
        validSubset(nums,subs,indx+1,total)
        
        # back track
        subs.pop()
        total -= nums[indx]
        
        validSubset(nums,subs,indx+1,total)
    validSubset(nums,[],0,0)
    return len(res)


nums = [5, 2, 3, 10, 6, 8]
target = 10

print(perfectSum(nums,target))