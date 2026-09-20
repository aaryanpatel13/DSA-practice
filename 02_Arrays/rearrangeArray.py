#               REARRANGE ARRAY ELEMETNS BY SIGN
""" 
Given an array 'nums' of size even interger. No.of positve element == No. of negative element
 Modify the array such that:
1. Every consecutive pair of integers have opposite sign.
2. Maintain the order of interger as they were present in the actual array
3. Modified array begins with the posiitve integer

Input: nums = [3,1,-2,-5,2,-4]
Output [3,-2,1-5,2,-4]; Order of positive integer:[3,1,2] & Order of negative integer: [-2,-5,-4]

"""
#                           BRUTE FORCE APPROACHED
# Store the order of positive and negative integer . Placed them one by one back to the main array in alternate order.

def rearrangeArray(nums):
    n = len(nums)
    positive = []
    negative = []
    for i in range(n):
        if nums[i] > 0:
            positive.append(nums[i]) # Storing the positve integer to record it's order
        else:
            negative.append(nums[i]) # Storing the negative integer to record it's order
    for i in range(n//2):
        nums[2*i] = positive[i]     
        nums[2*i+1] = negative[i]
    return nums



#                                            OPTIMAL APPROACH

# Create a new array and iterate through the actual array. If the element is positive 
# store it at the positive index of new array and Increase the positive index by 2 .
#  Do the smae for nefative index if the element is negative.

def rearrangeArray(nums):
    n = len(nums)
    ans = [0] * n
    pos_indx = 0
    neg_indx = 1
    for i in range(n):
        if nums[i] > 0:
            ans[pos_indx] = nums[i]
            pos_indx += 2
        else:
            ans[neg_indx] = nums[i]
            neg_indx += 2
    return ans



nums = [3,1,-2,-5,2,-4]
print(rearrangeArray(nums))


#               Type 2 of this question : NO. OF POSITIVE ELEMENT != NO. OF NEGATIVE ELEMENT

# Input : nums = [1,2,3,-4,-1]
# Output: [1,-4,2,-1,3]

def rearrangeArray(nums):
    n = len(nums)
    pos = []
    neg = []
    for i in range(n):
        if nums[i] > 0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])
        
    i = j = 0
    ans = []

    while i < len(pos) and j < len(neg):
        ans.append(pos[i])
        i += 1

        ans.append(neg[j])
        j += 1

    while i < len(pos):
        ans.append(pos[i])
        i += 1
    
    while j < len(neg):
        ans.append(neg[j])
        j += 1
    return ans

nums = [1,2,3,-4,-1]
print(rearrangeArray(nums))
