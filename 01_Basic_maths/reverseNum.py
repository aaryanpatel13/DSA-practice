#Input: n = 1234
#Output: 4321

def reverseNum(n):
    rev_num = 0
    while n > 0:
        lst_digit = n%10
        rev_num = rev_num * 10 + lst_digit
        n = n//10
    return rev_num

n = 25
print(reverseNum(n))
    