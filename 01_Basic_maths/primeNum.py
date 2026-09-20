def isPrime(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
    



#                       BETTER APPROACH
from math import sqrt
def isPrime(n):
    count = 0
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            count += 1
            if n/i != i:
                count += 1
    if count == 2:
        return True
    else:
        return False
n = 11
print(isPrime(n))