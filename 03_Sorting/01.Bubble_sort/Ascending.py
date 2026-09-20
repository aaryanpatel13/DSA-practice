# ASCENDING ORDER USING BUBBLE SORT
# nums = [5,2,3,1]

nums = [5,2,3,1]
print(f"Given array: {nums}")
def bubbleSort(nums):
    n = len(nums)
    for i in range(n):
        isSwap = False                      #Ye help krega check krne m ki sort hote hi loop break ho jae
        for j in range(0, n-i-1):           # j loop 0 se har baar last second position tk chlna
            if nums[j] > nums[j+1]:         #swap
                temp  = nums[j]             #python m swap krne k liye ye bhi likha ja skta hai
                nums[j] = nums[j+1]         #nums[j], nums[j+1] = nums[j+1], nums[j]    
                nums[j+1] = temp        
                isSwap = True
            
        if not isSwap :                     #incase array phle se sorted ho
            break
            
    return(nums)

print(f"Sorted array: {bubbleSort(nums)}")