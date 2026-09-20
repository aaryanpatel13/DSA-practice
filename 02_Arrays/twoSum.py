#Given an array and a target . Return the indices of those two element whhich sum == target.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

#                               BRUTE FORCE APPROACH 
# Take one element and add it with rest of the other element from the array and check if sum == target.

def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if (nums[i] + nums[j] == target):
                return i,j




#                                   BETTER APPROACH [Hashing]
# This can be cosidered as the Optimal appraoch if the array is not sorted.
def twoSum(nums,target):
    n = len(nums)
    check_map = {}
    for i in range(n):
        rem = target - nums[i]
        if rem in check_map:
            return check_map[rem],i
        if nums[i] not in check_map:
            check_map[nums[i]] = i



#                                   OPTIMAL APPROACH [Two Pointers approach]
#                              [ WORKS ONLY WHEN GIVEN ARRAY IS ALREADY SORTED ]
def twoSum(nums,target):
    n = len(nums)
    left = 0
    right = n-1
    while left < right:
        sm = nums[left] + nums[right]

        if sm == target:
            return left, right
        
        if sm > target:
            right -= 1
        else:
            left += 1
# EXAMPLE          
nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))
    