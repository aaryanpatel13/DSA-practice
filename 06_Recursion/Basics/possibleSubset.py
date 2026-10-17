                                        #SUBSET SUM 2

                                    # TYPE 1: Return list of all possible subset
"""
Given an arrya 'nums'. Return list of all possible subset
Input: nums = [1,2,2]
Output:[[1, 2, 2], [1, 2], [1, 2], [1], [2, 2], [2], [2], []] ---> This can be in any order

"""

def possible_subset(nums):
    n = len(nums)
    ans = []
    def subSet(indx,sbset):
        if indx == n:
            ans.append(sbset.copy())
            return
        # PICK
        sbset.append(nums[indx])
        subSet(indx+1,sbset)
        sbset.pop()

        # NOT PICK
        subSet(indx+1,sbset)

    subSet(0,[])
    return ans

nums = [1,2,2]
print(possible_subset(nums))
        



#                            TYPE 2: Return the list of all possible subset but it does not contain duplicates.
# INPUT: nums = [1,2,2]
# OUPUT:[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]


def possible_subset(nums):
    nums.sort()
    n =len(nums)
    ans = []
    def subSet(indx,sbset):
            ans.append(sbset.copy())
            for i in range(indx,n):
                 # check for duplicates
                 if i > indx and nums[i] == nums[i-1]:
                      continue
                 
                 #pick
                 sbset.append(nums[i])
                 subSet(i+1,sbset)
                 sbset.pop()
    subSet(0,[])
    return ans
                 
     
nums = [1,2,2]
print(possible_subset(nums))



