"""
Given a pair of strings s1 and s2 of equal lengths, your task is to find which of the two strings has more distinct subsequences. If both strings have the same number of distinct subsequences, return s1.

Examples:

Input: s1 = "gfg", s2 = "ggg"
Output: "gfg"
Explanation: "gfg" have 6 distinct subsequences whereas "ggg" have 3 distinct subsequences.
 
"""
# This is not good for big strigns ....badi strings k liye DP use krna hoga
def generateSubse(string):          # this will help us to know how many unique strings can be created from given string
    n = len(string)
    ans = set()
    def generate(indx,subs):
        if indx == n:
            ans.add("".join(subs))
            return
        
        subs.append(string[indx])
        generate(indx+1,subs)
        
        subs.pop()
        
        generate(indx+1,subs)
        
    generate(0,[])
    return(len(ans))



def betterString(s1,s2):
    s1_ = generateSubse(s1)
    s2_ = generateSubse(s2)
    
    if s1_ >= s2_:
        print(s1)
    else:
        print(s2)
    

s1 = "gfg"
s2 = "ggg"

betterString(s1,s2)