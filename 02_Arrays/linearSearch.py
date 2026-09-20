#Input: nums = [2,3,4,5,3,2], taget = 3
#Output: 1 ; Return the smallest index where the target appears in the array.
def linearSearch(nums,target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i 
          
    return -1

#EXAMPLE 
nums = [1,2,3,4,3,5]
target = 5
print(linearSearch(nums,target))