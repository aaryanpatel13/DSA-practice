# DESCENDING ORDER USING BUBBLE SORT
# nums = [5,2,3,1]

nums = [5, 2, 3, 1]
print(f"Given array: {nums}")

def bubbleSortDescending(nums):
    n = len(nums)
    for i in range(n):
        isSwap = False  # Check if any swap happens in this pass
        for j in range(0, n - i - 1):
            if nums[j] < nums[j + 1]:  # Change comparison for descending
                # Swap
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                isSwap = True

        if not isSwap:  # If no swaps, array is sorted
            break


    return nums

print(f"Sorted array (Descending): {bubbleSortDescending(nums)}")