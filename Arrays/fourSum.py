"""
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
1. 0 <= a, b, c, d < n
2. a, b, c, and d are distinct.
3. nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

"""
#                                   BRUTE FORCE APPROACH
#                                   Time Complexity: O(N^4)
#                                   Time Complexity: O(N)

def fourSum(nums, target):
    n = len(nums)
    nums.sort()
    ans = set()
    
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if nums[i] + nums[j]+nums[k]+nums[l] == target:
                        temp = [nums[i],nums[j],nums[k],nums[l]]
                        temp.sort()
                        ans.add(tuple(temp))
    return [list(res) for res in ans]

nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums,target))
                    
                    
                    
#                                   Better FORCE APPROACH
#                                   Time Complexity: O(N^3)
#                                   Time Complexity: O(N)

def fourSum(nums, target):
    n = len(nums)
    nums.sort()
    ans = set()
    
    for i in range(n):
        for j in range(i+1,n):
            track = set()
            for k in range(j+1,n):
                fourth = target - (nums[i] + nums[j] + nums[k])
                if fourth in track:
                    temp = [nums[i], nums[j],nums[k],fourth]
                    temp.sort()
                    ans.add(tuple(temp))
                track.add(nums[k])
    return [list(res) for res in ans]

nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums,target))


#                                   OPTIMAL FORCE APPROACH
#                                   Time Complexity: O(N^3)
#                                   Time Complexity: O(N) --> This is reuiqred to return the answer


def fourSum(nums,target):
    n = len(nums)
    ans = []
    nums.sort()
    
    for i in range(n):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n):
            if j != 1 and nums[j] == nums[j-1]:
                continue
            k = j+1
            l = n-1
            
            while k < l:
                sm = nums[i] + nums[j] + nums[k] + nums[l]
                
                # IF total sum > target
                if sm < target:
                    k += 1
                elif sm > target:
                    l -= 1
                else:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    ans.append(temp)
                    k += 1
                    l -= 1
                    # Avoid duplicates for k
                    while k < l and nums[k] == nums[k-1]:
                        k += 1
                    # Avoids duplicates for L
                    while k < l and nums[l] == nums[l+1]:
                        l -= 1
    return ans

nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums,target))
                 