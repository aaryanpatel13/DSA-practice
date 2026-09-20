def gcd(n1,n2):
    ans = 1
    n = min(n1,n2)
    for i in range(n,0,-1):
        if n1 % i == 0 and n2 % i == 0:
            ans = i
            return ans
        



# BETTER APPROACH EUCLIDEAN ALGORITHM
def gcd(a,b):
    while a > 0 and b > 0:
        if a>b:
            a = a%b
        else: 
            b = b % a
    if (a == 0):
        return b
    return a

n1 = 52
n2 = 10
print(gcd(n1,n2))