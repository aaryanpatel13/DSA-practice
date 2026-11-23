"""
Given an integer n. You need to generate all the binary strings of n characters representing bits.
Note: Return the strings in  ascending order.
Example:
Input: n = 2
Output: [00, 01, 10, 11]
Explanation: As each position can be either 0 or 1, the total possible combinations are 4.

"""

def generate(s,n,ans):
    if len(s) == n:
        ans.append(s[:])
        return
    
    generate(s +"0",n,ans)
    generate(s +"1",n,ans)
    
    return sorted(ans)

n = 2
print(generate("", n, []))