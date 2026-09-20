""" Given an array 'nums' and opreations 'k'. Choose one target element and do INCREMNET operations  on the other elements 
so that the target element become the most occuring element in the array.
Return the target and it's frequency """
#Input: nums = [1,2,4] , k = 5
#Output: target: 4, freq: 3
# Explain: Increment nums[0] by 3 times and nums[1] by 2 times to make nums = [4,4,4]

                                # SLIDING WINDOW APPROACH
def maxFrequency(nums,k):
    nums.sort()
    n = len(nums)
    left = 0 
    total = 0
    freq = 1
    target = nums[0]

    for right in range(n):
        total += nums[right]

        cost = nums[right] * (right-left+1) -total
        #Valid window conditon
        while cost > k:
            total -= nums[left]
            left += 1
            cost = nums[right] * (right-left+1) -total
        # MAX Freq update 
        if (right-left+1) > freq:
            freq = right -left +1
            target = nums[right]        # Track target


    return target , freq


nums = [1,2,4]
k = 5
target,freq = maxFrequency(nums,k)
print(f"Target: {target}")
print(f"freq: {freq}")



