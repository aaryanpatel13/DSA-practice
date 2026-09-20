def rotateArray(nums,k):
    n = len(nums)
    k = k%n
    first = nums[:k]
    first.reverse()

    second = nums[k:]
    second.reverse()

    result = first + second
    result.reverse()
    
    return result

#EXAMPLE
k = int(input("Enter the value for rotation: "))
nums = [1,2,3,4,5,6,7]
rotate = rotateArray(nums,k)
print(rotate)