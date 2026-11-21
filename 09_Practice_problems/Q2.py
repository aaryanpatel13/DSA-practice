"""
Express number as a sum of two prime numbers
Example:
Input: 34
Output: 3 and 31
"""

def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

def primeSum(num):
    for i in range(2,num):
        if isPrime(i) and isPrime(num - i):
            return f"{i} and {num-i}"
        
num = 7
print(primeSum(num))
    