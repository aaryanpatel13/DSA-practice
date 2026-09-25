#                             81. Search in Rotated Sorted Array II
"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.

Example :
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

"""
def search(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    while low <+ high:
        mid = (low + high)//2
        
        if nums[mid] == target:     # target found
            return True
        # Condition to eleminate the dupplicates
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            
        elif nums[low] <= nums[mid]:  # Check if left part is sorted?
            if nums[low]<= target <= nums[mid]:  # if target is in the left part?
                high = mid - 1      # check in the left part
            else:
                low = mid + 1               # check in the right part
        else:                   # right part of the array is sorted
            if nums[mid ]<= target <= nums[high]:       # target is in the right part
                low = mid + 1                   # check in the right part
            else:
                high = mid - 1                  # check in the left part
    return False

nums = [2,5,6,0,0,1,2]
target = 7
print(search(nums,target))