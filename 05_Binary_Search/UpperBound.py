"""
You are given a sorted array nums[] containing n integers and a integer target x.
Implement the upper bound function to find the index of the upper bound of x in the array.

Note:
1. The upper bound in a sorted array is the index of the first value that is greater than a given value. 
2. If the greater value does not exist then the answer is 'n', Where 'n' is the size of the array.
3. Try to write a solution that runs in log(n) time complexity.

Example:
Input : nums = {2,4,6,7} and x = 5,
Output: 2
Explanation: The upper bound of 5 is 6 in the given array, which is at index 2 (0-indexed).

"""
def upperBound(nums,x):
    n = len(nums)
    low = 0
    high = n-1
    ans = n
    
    while low <= high:
        mid = (low + high)//2
        
        if nums[mid] > x:           # upper bound means strictly greater than target
            ans = mid               # element > target ; check in the left part 
            high = mid - 1
        else:
            low = mid + 1       # element <= target; check in the right part
    return ans


nums = [1,1,2,3,4,5,5,6,7]
x = 3
print(upperBound(nums,x))