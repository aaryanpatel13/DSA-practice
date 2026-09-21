#                           FLOOR in SORTED ARRAY
"""
Given a sorted array nums[] and an integer x, 
find the index (0-based) of the largest element in arr[] that is less than or equal to x.
This element is called the floor of x. If such an element does not exist, return -1.

Input: nums[] = [1, 2, 8, 10, 10, 12, 19], x = 5
Output: 1
Explanation: Largest number less than or equal to 5 is 2, whose index is 1.

"""

def floor(nums,x):
    n = len(nums)
    low = 0
    high = n-1
    ans = -1
    
    while low <= high:
        mid =(low+high)//2
        
        if nums[mid] == x:          
            ans = mid               # keep this as answer
            low = mid+1             # keep checing in the right part of array
        elif nums[mid] > x:         # Answer is in the left part of the array    
            high = mid -1
        else:
            ans = mid               # Smaller element found; keep this and check in the right part of the array 
            low = mid +1
    return ans
            
nums = [1, 2, 8, 10, 10, 12, 19]
x = 5
print(floor(nums,x))

