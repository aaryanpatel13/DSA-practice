#DESCENDIGN ORDER
def partition(nums,low,high):
    pivot = nums[low]
    i = low
    j = high
    while(i<j):
        while pivot <= nums[i] and i <= high - 1:
            i = i+1
        while pivot > nums[j] and j >= low +1:
            j = j-1 
        if (i<j):
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]

    return j
    
def quick_sort(nums,low,high):
    #Base case
    if low>= high:
        return
    
    #Recursive case
    p = partition(nums,low,high)
    quick_sort(nums,low,p-1)
    quick_sort(nums,p+1,high)

    return nums

#USE CASE
nums = [10,7,8,9,1,4]
sorted_array = quick_sort(nums,0,len(nums)-1)
print(f"Sorted array is : {sorted_array}")