#                                   COMBINATION SUM 2 
# TYPE 1: Element can be used only once 
#          The Output must not contain any duplicates
"""
Given an array of distinct integers candidates and a target integer target.
Return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

EXAMPLE:
Input: nums = [10,1,2,7,6,1,5], target = 8
Output:[ [1,1,6], [1,2,5], [1,7], [2,6] ]

"""
def combinationSum(nums,target):
    nums.sort()                                 # Same elements will comes next to each other
    res = []                                    #Sorting will help to get early break condition while removing duplicates
    def combination(indx,target,combi):
        if target == 0:
            res.append(combi.copy())
            return
        
        for i in range(indx,len(nums)):
            # skip duplicates
            if i > indx and nums[i] == nums[i-1]:
                continue
            # stop if element is greater than target
            if nums[i] > target:
                break

            # Pick element
            combi.append(nums[i])
            combination(i+1,target - nums[i], combi)
            combi.pop()

    combination(0,target,[])
    return res

nums = [10,1,2,7,6,1,5]
target = 8
print(combinationSum(nums,target))