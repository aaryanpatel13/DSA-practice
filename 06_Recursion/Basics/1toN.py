def printNum(i,n):
    if i > n:
        return
    print(i)
    printNum(i+1,n)


n = 10
printNum(1,n)
