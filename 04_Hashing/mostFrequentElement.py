def mostFrequentElement(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    most_occured = max(freq, key = freq.get)
    return most_occured

nums = [1,2,3,2,3,2,2,4,5]
print(mostFrequentElement(nums))