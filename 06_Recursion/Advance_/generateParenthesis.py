"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

"""

#                                   UISNG ONLY ONE COUNTER(total)
def solve(indx,total,brc,res):
    if indx == len(brc):
        if total == 0:
            res.append("".join(brc))
        return
    
    if total > len(brc) // 2:    
        return
    
    if total < 0:
        return
    
    brc[indx] = "("
    solve(indx+1,total + 1,brc,res)
    
    if total > 0:
        brc[indx] = ")"
        solve(indx +1, total - 1, brc, res) 
        
    
def generateParenthesis(n):
    brackets = [""] * (n * 2)  # Array of size 2n for n pairs
    result = []                # List to store all valid combinations
    solve(0, 0, brackets, result)  # Start with index 0, total 0
    return result

                
print(generateParenthesis(3))        



#                                   UISNG TWO COUNTERs(open, close)

def generateParenthesis(n):
    ans = []
    def generate(s,open,close):
        
        if len(s) == 2*n:
            ans.append(s[:])
            return
        
        if open < n:
            s += "("
            open += 1
            generate(s,open,close)
            
        if close < open:
            s += ")"
            close += 1
            generate(s,open,close)
            
    generate("",0,0)
    return ans


print(generateParenthesis(3))