
# Convert Decimal to Binary
def dec2binary(num:int) -> str:
    ans = ""
    while num > 0:
        if num % 2 == 1:
            ans += "1"
        else:
            ans += "0"
        num = num // 2
        
    ans = ans[::-1]
    return ans
print(dec2binary(13))

# Convert Binary to Decimal
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
        
# Swap two numbers using bit manipulation [By using XOR operator] ^ ---> this is XOR operator
def swap(a,b):
    print(f"current a & b: {a,b} \n")
    a = a^b
    b = a^b
    a = a^b
    print(f"swapped a & b: {a,b} \n")

swap(10,15)

# Check if the ith bit is set or not? 1--> mtlb bit is set & 0 --> mtlb bit is not set
def isSet(num,i):       # using left shift operator (<<)
    if (num & (1 << i)) != 0:
        return True
    return False


def isSet(num,i):       # using right shift operator (>>)
    if(num >> i) & 1 == 1:
        return True
    return False


