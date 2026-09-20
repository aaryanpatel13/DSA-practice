#DESCENDING ORDER
def merge(left,right):
    result = []
    i = j = 0

    n = len(left)
    m = len(right)

    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i =+ 1
        else:
            result.append(right[j])
            j =+1

        if i < n:
            result.append(left[i])
            i = i+1
        
        if j < m:
            result.append(right[j])
            j = j+1

    return result
def merge_sort(nums,low,high):
    if low >= high:
        return [nums[low]]
    mid = (low+high)//2

    left = merge_sort(nums,low,mid)
    right = merge_sort(nums,mid+1,high)

    sorted_array = merge(left,right)

    return sorted_array

# USE CASE
nums = [9,4,5,7,3,7,2,]
sorted_array = merge_sort(nums,0,len(nums)-1)

print(f"Given array: {nums}")
print(f"Sorted array: {sorted_array}")

