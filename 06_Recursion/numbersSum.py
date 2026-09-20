# SUM OF first N numbers


#                           Parameterised Recursion [We print the result from the function]
def numbersSum(i,sum):
    sm = 0
    if i < 1:
        print((sum))
        return
    numbersSum(i-1,sum+i)
#TEST CASE
n = 4
numbersSum(n)

#                   Functional Recursion [We return the result from the funciton]
def numbersSum(n):
    if n == 0:
        return 0
    else:
        return (n +numbersSum(n-1))
#TEST CASE
n = 4
print(numbersSum(n))
