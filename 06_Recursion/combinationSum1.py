#                                   COMBINATION SUM 1
# TYPE 1: Element can be use many times
"""
Given an array of distinct integers candidates and a target integer target.
Return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

EXAMPLE:
Input: nums = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

"""

def combinationSum(nums,target):                            # main function defination
    res = []
    def combination(indx,target,combi):                    #  Inner Recursive function
        
        if target == 0:                                    # Base Case 1
            res.append(combi.copy())                   # WHENEVER STORING A MUTABLE LIST IN RESULT ; ALWAY STORE .copy() 
            return
        
        if indx == len(nums):                              # Base Case 2 
            return
        
        #Pick if possible                                   # Pick only when element is smaller than target
        if nums[indx] <= target:
            combi.append(nums[indx])
            combination(indx,target - nums[indx],combi)
            combi.pop()
        
        #Not pick
        combination(indx+1,target,combi)

    combination(0,target,[])                            # Calling inner recursive function
    return res


nums = [2,3,6,7]
target = 7
print(combinationSum(nums,target))

