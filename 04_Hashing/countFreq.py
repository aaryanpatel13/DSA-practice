# Counting Frequencies of Array Elements
# Given an array of size n whihc may contains duplicate elements.Return the [key,value] for the array where:
# key --> element of the array
# value --> frequency of that element

#Input: nums = [1,2,3,2,1,3,2,4]
#Output: [[1,2],[2,3],[3,2],[4,1]]

def countFreq(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    res = []
    for key,value in freq.items():
        res.append([key,value])
    
    return res

nums = [1,2,3,2,1,3,4,5]
print(countFreq(nums))

