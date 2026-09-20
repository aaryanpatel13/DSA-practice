#Input: n = 6
#Output: [1,2,3,6]

def divisors(n):
    for i in range(1,n+1):
        if n%i == 0:
            print(i)

#               BETTER APPROACH
from math import sqrt
def divisors(n):
    res = []
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            res.append(i)
            if n//i != i:
                res.append(n//i)
    res.sort()
    return res
    
n = 6
print(divisors(n))
