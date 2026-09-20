#Input: n = 14
#Output: 2

def digitCount(n):
    count = 0
    while n > 0:
        n = n//10
        count += 1
    return count


n = int(input("Enter n: "))
print(f"No. of digit: {digitCount(n)}")