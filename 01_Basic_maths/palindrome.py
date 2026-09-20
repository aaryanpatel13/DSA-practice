#Input: n =121
#Output: True
def palindrome(n):
    original = n
    rev_num = 0
    while n > 0:
        lst_digit = n%10
        rev_num = rev_num * 10 + lst_digit
        n = n//10
    if rev_num == original:
        return True
    else:
        return False

n = 122
print(palindrome(n))
