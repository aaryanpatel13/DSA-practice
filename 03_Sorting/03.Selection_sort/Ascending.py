# ASCENDING ORDER USING BUBBLE SORT
# nums = [5,2,3,1]

nums = [5,2,3,1]
print (f"given array: {nums}")

def selection_sort(nums):
    n = len(nums)
    
    for i in range(n):
        mins = nums[i]
        indx = i

        for j in range (i+1,n):
            if nums[j]<mins:
                mins = nums[j]
                indx = j

        temp = nums[i]
        nums[i] = nums[indx]
        nums[indx] = temp
    return nums


print(f"Sorted array: {selection_sort(nums)}")



