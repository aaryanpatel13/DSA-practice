"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

"""

#                                   BRUTE FORCE APPROACH
#                                   Time Complexity: O(N^3)
#                                   Time Complexity: O(N²)
def threeSum(nums):
    n = len(nums)
    ans = set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    ans.add(tuple(temp))
    return [list(res) for res in ans]



nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))


#                                   Better FORCE APPROACH
#                                   Time Complexity: O(N²)
#                                   Time Complexity: O(N²)
def threeSum(nums):
    n = len(nums)
    ans = set()
    for i in range(n):
        track = set()
        for j in range(i+1,n):
            third = -(nums[i] + nums[j])
            if third in track:
                temp = [nums[i], nums[j], third]
                temp.sort()
                ans.add(tuple(temp))
            track.add(nums[j])
    return [list(res) for res in ans]


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))



#                                   OPTIMAL FORCE APPROACH
#                                   Time Complexity: O(N²)
#                                   Time Complexity: O(1)

def threeSum(nums):
    n = len(nums)
    ans = []
    nums.sort()
    
    for i in range(n):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        
        #Two pointers
        j = i+1
        k = n-1
        while  j < k:
            sum = nums[i] + nums[j] + nums[k]
            
            if sum < 0:
                j += 1
            elif sum > 0:
                k -= 1
            else:
                temp = [nums[i],nums[j],nums[k]]
                ans.append(temp)
                j += 1
                k -= 1  
                #skip duplicates
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
    return ans

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))