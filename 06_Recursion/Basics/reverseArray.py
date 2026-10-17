# Recursive function using two pointers
def reverseArray(nums,l,r):
    if l > r :
        return
    nums[l], nums[r] = nums[r], nums[l]
    reverseArray(nums,l+1,r-1)

#TEST CASE
nums = [1,2,3,4]
reverseArray(nums,0,len(nums)-1)
print(nums)


# Recursive function using one pointer
def reverseArray(nums,i):
    n = len(nums)
    if i >= n//2:
        return
    nums[i], nums[n-i-1] = nums[n-i-1] , nums[i]
    reverseArray(nums,i+1)

nums = [1,2,3,4]
reverseArray(nums,0)
print(nums)