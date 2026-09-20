def fibonacciNum(n):
    if n <= 1:
        return n
    return fibonacciNum(n-1) + fibonacciNum(n-2)

n = 4
print(fibonacciNum(n))