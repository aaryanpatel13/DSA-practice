"""
Given an array 'nums' with 'n' objects colored red, white, or blue, sort them in-place 
so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
"""
# Input: nums = [2,0,2,1,1,0,2]
# output: [0,0,1,1,2,2,2]




# BRUTE FORCE APPROACH : Use any sorting method like Merge asort or Quick sort to sort the array.


#BETTER APPROACH:
""" Use 3 count variable : c0 for no. of 0's ; c1 for no. of 1's and c2 for no. of 2's
    Iterate through the array and increase the count variable to k now the exact count of each elements.
    Then put them in the new array.
"""
def sortColors(nums):
    n = len(nums)
    c0 = 0
    c1 = 0
    c2 = 0

    for i in range(n):
        if nums[i] == 0:
            c0 += 1
        
        elif nums[i] == 1:
            c1 += 1
        else: 
            c2 += 1
    for i in range(c0):
        nums[i] = 0
    
    for i in range(c0,c0+c1):
        nums[i] = 1
    for i in range (c0+c1,n):
        nums[i] = 2
    return nums


#                                       OPTIMAL APPROACH
#                                   DUTCH NATIONAL FLAG ALGORITHM
# Three ponters approach :mleft,mid and high.

def sortColors(nums):
        n = len(nums)
        low = mid = 0
        high = n-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

nums = [2,0,2,1,1,0,2]
sortColors(nums)
print(nums)
