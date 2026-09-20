#Transpose the given matrix or 2D list
nums  = [[1,2,3],[4,5,6],[7,8,9]]

rows = len(nums)
cols = len(nums[0])

res = [[0]*rows  for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        res[j][i] = nums[i][j]
print(res)