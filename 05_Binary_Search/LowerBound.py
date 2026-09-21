"""
Given a sorted array arr of n integers and an integer x, 
find the index of the lower bound of x : the first index where arr[i] >= x. 
Agar aisa koi element na ho, toh return n.

Input: arr = [1, 2, 2, 3, 5, 7], x = 4
Output: 4
Explanation: arr[4] = 5, jo x se >= hai, aur yeh pehla aisa index hai.

"""

def lowerBound(nums,x):
    n = len(nums)
    low = 0
    high = n-1
    ans = n
    while low <= high:
        mid = (low + high)//2
        
        if nums[mid] >= x:              #lower bound means first element >= target
            ans = mid                   # element >= target; check in the left part to more
            high = mid - 1
        else:
            low = mid + 1               # element < target; check in the right part for ans
    return ans

nums = [1, 2, 2, 3, 5, 7]
x = 4
print(lowerBound(nums,x))