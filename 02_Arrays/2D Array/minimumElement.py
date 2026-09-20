# Find the minimum element of given list

nums = [[10,25,3,8],[7,12,5,6],[9,0,18,30]]
rows = len(nums)
cols = len(nums[0])
minimum = 10 ** 18
for i in range(rows):
    for j in range(cols):
        if nums[i][j]<= minimum:
            minimum = nums[i][j]
print(minimum)