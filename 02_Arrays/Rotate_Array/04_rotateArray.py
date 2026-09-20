def reverse(nums,start,end):
    n = len(nums)
    while start < end:
        temp = nums[start]
        nums[start] = nums[end-1]
        nums[end-1] = temp
        start += 1
        end -= 1
    return nums
def rotateArray(nums,k):
    n = len(nums)
    k = k % n

    reverse(nums,0,n-k)
    reverse(nums,n-k,n)
    reverse(nums,0,n)
    return nums

k = int(input("Enter the value for rotation: "))
nums = [1,2,3,4,5,6,7]
rotateArray(nums,k)
print(nums)