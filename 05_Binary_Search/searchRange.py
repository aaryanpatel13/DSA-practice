#                       34. Find First and Last Position of Element in Sorted Array
"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

"""
def lowerBound(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    lb = -1
    while low <= high:
        mid = (low+high)//2
        if nums[mid]>= target:
            lb = mid
            high = mid -1
        else:
            low = mid + 1
    return lb               # this is the starting index of target


def upperBound(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    ub = n
    while low <= high:
        mid = (low+high)//2
        if nums[mid] > target:
            ub = mid
            high = mid -1
        else:
            low = mid + 1
    return ub           # this is the first element > target

def searchRange(nums,target):
    lb = lowerBound(nums,target)
    ub = upperBound(nums,target)
    if lb == -1 or nums[lb] != target:
        return -1
    else:
        return [lb,ub-1]                # range = [lb,ub-1]
    
nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums,target))
    

