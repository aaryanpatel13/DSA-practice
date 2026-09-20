#Input: nums= [1,2,3,4,5]
#output: True ; nums is sorted here
def isSorted(nums):
    n = len(nums)
    for i in range (1,n):
        if nums[i]>= nums[i-1]:
            i += 1
        else:
            return False
    return True


#EXAMPLE
nums = [1, 2, 3, 4, 5]
check = isSorted(nums)
print(check)