#                                Ceil The Floor
"""
You're given a sorted array nums of 'n' integers and an integer target 'x'.
Find the floor and ceiling of 'x' in 'a[0..n-1]'.

Note:
Floor of 'x' is the largest element in the array which is smaller than or equal to 'x'.
Ceiling of 'x' is the smallest element in the array greater than or equal to 'x'.

Example:
Input: nums = [3,4,4,8,9,9,10,12,12,14,15], x = 6
Output: [4,8]

"""
def FloorAndCeil(nums,x):
    n = len(nums)
    low = 0
    high = n-1
    floor = -1
    ceil = -1
    while low <= high:
        mid = (low + high)//2
        
        if nums[mid] == x:
            floor = nums[mid]
            ceil = nums[mid]
            return [floor,ceil]
        elif nums[mid] > x:
            ceil = nums[mid]
            high = mid - 1
        else:
            floor = nums[mid]
            low = mid + 1
    return [floor,ceil]
            
nums = [3,4,4,8,9,9,10,12,12,14,15]
x = 6
print(FloorAndCeil(nums,x))