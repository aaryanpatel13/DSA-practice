#                                       BRUTE FORCE APPROACH    
def missingNnumber(nums):
    n = len(nums)
    for i in range(n+1):
        flag = 0
        for j in range(n):
            if nums[j] == i:
                flag = 1
                break
        if flag == 0:
            return i
    
#                                   BETTER APPROACH
def missingNumber(nums):
    n = len(nums)
    hash_map = [0]* (n+1)
    for num in nums:
        hash_map[num] = 1
    for i in range(n+1):
        if hash_map[i] == 0:
            return i


#                                   OPTIMAL APPROACH--1
def missingNumber(nums):
    n = len(nums)
    sum1 = (n*(n+1))//2
    sum2 = 0
    for i in range(n):
        sum2 += nums[i]
    return(sum1 - sum2)



#                               MOST OPTIMAL APPROACH
def missingNumber(nums):
    n = len(nums)
    xor1 = 0
    xor2 = 0
    for i in range(n):
        xor2 = xor2 ^ nums[i]
        xor1 = xor1 ^ i+1
    
    return xor1 ^ xor2


#EXAMPLE 
nums = [0,1,3,2]
print(missingNumber(nums))

