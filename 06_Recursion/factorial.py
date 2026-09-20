# Parameterised Recursion
def factorial(i,product):
    if i <1:
        print(product)
        return
    factorial(i-1,product = product * i)
#TEST CASE
n = 3
factorial(n,1)

# Funcitonal Recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
#TEST CASE
n = 5
print(factorial(n))





