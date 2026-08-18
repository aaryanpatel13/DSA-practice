# '''
# Given an array 'nums' of distinct integers, return all the possible permutation.
# ex: nums = [1,2,3]
# output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# '''

#                             #Type 1: Using extra space [One hash map to track path is used]
# def permutation(nums):
#     n = len(nums)
#     ans = []
    
#     def check(path):
#         if len(path) == n:
#             ans.append(path[:])         # store copy of path as we are goinng to alter it.
#             return 
        
#         for num in nums:
#             if num in path:
#                 continue
            
#             path.append(num)
#             check(path)
#             path.pop()
#     check([])
#     return ans


# #TEST
# nums = [1,2,3]
# print(permutation(nums))



                        #Type 2: Without using any extra space. Just by Swapping
                        
def permutation(nums):
    n = len(nums)
    ans = []
    def swap(indx):
        if indx == n:
            ans.append(nums[:])
            return
        for i in range (indx,n):
            nums[indx], nums[i] = nums[i], nums[indx] # SWapping nums[indx] & nums[i]
            
            swap(indx+1) # increaing indx by 1 to check for next item
            
            nums[indx], nums[i] = nums[i], nums[indx] # Backtracking
    swap(0)
    return ans