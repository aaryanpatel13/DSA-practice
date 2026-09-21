#                           35. Search Insert Position
"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index where it would be if 
it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2

"""

def searchInsert(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    ans = n    
    while low <= high:
        mid = (low + high)//2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            ans = mid
            high = mid -1
        else:
            low = mid + 1
    return ans

nums = [1,3,5,6]
target = 4
print(searchInsert(nums,target))