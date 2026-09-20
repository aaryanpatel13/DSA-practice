                                        #SUBSET SUM 1
"""
Given an arrya 'nums'. Print the sum of each possible subset
Input: nums = [2,3]
Output: 0 ,2,3,5
Explanation: [],[2],[3],[2,3] These are the possible subset of given array 

"""

def subsetSum(nums):
    ans = []
    n =len(nums)

    def subSet(indx,sum):
        if indx == n:
            ans.append(sum)
            return
            #PICK
        subSet(indx+1,sum + nums[indx])
            

            #NOT PICK
        subSet(indx+1,sum)
    subSet(0,0)
    ans.sort()
    return ans

nums = [2,3]
print(subsetSum(nums))
    