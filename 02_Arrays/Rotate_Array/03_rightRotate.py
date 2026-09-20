def rotateArray(nums,k):
    n = len(nums)
    k = k%n
    first = nums[:n-k]
    first.reverse()

    second = nums[n-k:]
    second.reverse()

    result = first + second
    result.reverse()

    nums[:] = result  # isse kuchh nya nhi bna...nums[] k andr k sare element result k sath replace hogye
    # return nums      isse better hua yhn pe

#EXAMPLE
k = int(input("Enter the value for rotation: "))
nums = [1,2,3,4,5,6,7]
rotateArray(nums,k)
print(nums)