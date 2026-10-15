"""
Convert a decimal number into binary number
Example:
Input: 13
Output: 1101

"""

# def dec2binary(num:int) -> str:
#     ans = ""
#     while num > 0:
#         if num % 2 == 1:
#             ans += "1"
#         else:
#             ans += "0"
#         num = num // 2
        
#     ans = ans[::-1]
#     return ans


# print(dec2binary(13))


def bin2Decimal(nums:str) -> int:
    ans = 0
    power = 0
    indx = len(nums) -1
    while indx >= 0:
        num = int(nums[indx]) * (2 ** power)
        ans += num
        indx -= 1
        power += 1    
    return ans

print(bin2Decimal("1101"))
        
