#Input: n = 153
#Output: True ; 1^3 + 5^3 + 3^3. =153

def armstrong(n):
    original = n
    sm = 0
    while n > 0:
        lst_digit = n%10
        sm += lst_digit * lst_digit * lst_digit
        n = n//10
    return sm == original


n = 151
print(armstrong(n))