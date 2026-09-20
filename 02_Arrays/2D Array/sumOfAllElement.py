# Find the total sum of given list

nums = [[1,2,3],[4,5,6],[7,8,9]]
rows = len(nums)
cols = len(nums[0])
sum = 0
for i in range(rows):
    for j in range(cols):
        sum += nums[i][j]
print(sum)