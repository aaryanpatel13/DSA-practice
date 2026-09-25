#                           Number of Occurrence
"""
Given a sorted array arr[] and a number target, find the number of occurrences of target in given array.

Examples:
Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4. 

"""
def lowerBound(self,arr,target):        # Helper function: this will return the starting index of target
    n = len(arr)
    low = 0
    high = n-1
    lb = -1                             # default value when target is found
    while low <= high:
        mid = (low + high)//2
        if arr[mid] >= target:
            lb = mid                   # it might be the answer
            high = mid-1               # Check in the left part of the array
        else:                          # arr[mid] < target
            low = mid + 1
    return lb
    
def upperBound(self,arr,target):       # Helper func: this will tell the index of first element > target
    n = len(arr)
    low = 0
    high = n-1
    ub = n                  # default answer ; when all element > target
    while low <= high:
        mid = (low + high)//2
        if arr[mid] > target:
            ub = mid            # it might be the answer
            high = mid-1        # keep checking in the left part of the arrayy
        else:                   # arr[mid] < target
            low = mid + 1
    return ub

def countFreq(self, arr, target):           # main function: this will return the no. of times target occured
    lb = self.lowerBound(arr,target)        # Starting index of the target 
    ub = self.upperBound(arr,target)        # Index of the first element > target
    
    if lb == -1 or arr[lb] != target:
        return 0
    else:
        return (ub-lb)                  # No. of times target occured
    