#Input: nums = [1,2,2,3,4,5,5]
# Output: 4 ; There are 4 uimique element in the given array 
def removeDuplicates(nums):
    n = len(nums)
    i = 0
    for j in range(1,n):
        if nums[j] != nums[i]:
            nums[i+1] = nums[j]
            i +=1
    return i+1
    

nums = [1,1,1,1,1]
check = removeDuplicates(nums)
print(check)