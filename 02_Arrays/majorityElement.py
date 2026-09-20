# Given an array 'nums' of size 'N'. The element whihc appears more than N/2 times in the array is the majority element.
# Input: nums = [2,3,2,1,2]
# Output: 2


#                               BRUTE FORCE APPROACH
#CHECK  EACH ELEMENT ONE BY ONE

def majorityElement(nums):
    n = len(nums)
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1
        if count > n//2:
            return nums[i]
        


#                               BETTER APPROACH [HASHING]
def majorityElement(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
        majority = max(freq, key = freq.get)            # key = freq.get will compare the frequncy and 
                                                        #return the key having maximum frequency
        return majority

nums = [2,3,2,1,2]
print(majorityElement(nums))


#                                   OPTIMAL SOLUTION
#                               MOORE'S VOTING ALGORITHM

def majorityElement(nums):
    n = len(nums)
    element = None
    count = 0
    for i in range(n):
        if count == 0:
            element = nums[i]
            count = 1
        elif nums[i] == element:
            count +=1
        else:
            count -= 1
    return element


# EXAMPLE
nums = [2,1,2,1,1]
print(majorityElement(nums))
        
