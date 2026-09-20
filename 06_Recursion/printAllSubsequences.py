#                                   PRINT ALL SUBSEQUENCES[PICK/ NOT PICK PATTERN]
"""
SUBSEQUENCE : A subsequnce is a sequence created by deleting zero or more elements from the given array without 
              changing the relative order of the remaining element.

EXAMPLE:
nums = [1,2,3]

valid susequence: [1,2] ---> we skipped 2 here, but maintain the order that 1 comes before 3.
Invalid subsequence:[3,1] ---> we skipped 2 here but order gets changed.


"""


def printSubs(nums,indx,subs):
    n = len(nums)
    # BASE CASE
    if indx == n:
        print(subs)
        return
    
    # Pick element
    subs.append(nums[indx])
    printSubs(nums, indx+1, subs)

    # Don't pick element
    subs.pop()
    printSubs(nums,indx+1,subs)

nums = [1, 2, 3]
printSubs(nums,0,[])