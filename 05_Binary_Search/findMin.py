#                       153. Find Minimum in Rotated Sorted Array
"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

"""
def findMin(nums):
    n = len(nums)
    low = 0
    high = n - 1
    mini = float("INF")             #Default minimum value
    while low <= high:
        mid = (low + high) // 2
        
        if nums[low] <= nums[mid]:          # If left part is sorted?
            mini = min(mini,nums[low])       # update mini
            low = mid + 1                   # check the right part for  element < mini
        else:                           # If right part is sorted?
            mini = min(mini,nums[mid]) # update mini
            high = mid - 1              # check the left for element < mini
    return mini


nums = [3,4,5,1,2]
print(findMin(nums))