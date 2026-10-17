#                                   COMBINATION SUM 3 

"""
Find the combination of 'k' numbers whose sum up to give 'n'. Return the list of all possible combinations.
Combinaiton should satisfy these condition:
1. Choose numbers from 1 to 9 only
2. Numbers should be used only for once
3. No duplicates are alloud as the output

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
"""

def combinationSum(k,n):
    res = []
    
    def combination(indx,target,combi):
        # BASE CASE
        if len(combi) == k:
            if target == 0:
                res.append(combi[:])
            return
        
        for num in range(indx,10):              # Range(indx,10) becoz wh have to pick number in b/w 1 to 9
            if num > target:
                break

            combi.append(num)
            combination(num+1,target-num,combi)
            combi.pop()
    combination(1,n,[])
    return res

k = 3
n = 7
print(combinationSum(k,n))