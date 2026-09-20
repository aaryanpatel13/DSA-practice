#Given in the array that every number will appears twice except for one.Find that single one
#Input: nums = [1,2,2,3,4,4,3]
#Output: 1 ; as it appears only for once



#                                    BRUTE FORCE APPROACH
def singleNumber(nums):
    n = len(nums)
    for i in range(n):
        freq = 0
        for j in range(n):
            if nums[j] == nums[i]:
                freq +=1
        if freq == 1:
            return nums[i]




#                                    BETTER APPROACH

def singleNumber(nums):
    #Create one empty map(dict)
    freq = {}
    #Store the frequency of element of the aray in the map
    for num in nums:
        freq[num] = freq.get(num,0)+1
    #if frequency ==1 , that's the number which appears only for once
    for num in freq:
        if freq[num] == 1:
            return num




#                            OPTIMAL APPROACH
def singleNumber(nums):
    n = len(nums)
    xor = 0
    for i in range(n):
        xor = xor ^ nums[i]
    return xor



#EXAMPLE
nums = [1,2,3,2,1,4,3]
print(singleNumber(nums))