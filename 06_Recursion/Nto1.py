def printNum(i,n):
    if i > n:
        return
    print(n)
    printNum(i,n-1)


n = 10
printNum(1,n)
