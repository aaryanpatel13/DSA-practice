def selection_sort(nums):
    n = len(nums)

    for i in range(n):
        key = nums[i]
        indx = i

        for j in range(i+1,n):
            if nums[j] > key:
                key = nums[j]
                indx = j
        
        nums[i],nums[indx] = nums[indx], nums[i]

    return nums


nums = [1, 2, 3, 5]

print(f"Given array: {nums}")
print(f"Sorted array: {selection_sort(nums)}")


