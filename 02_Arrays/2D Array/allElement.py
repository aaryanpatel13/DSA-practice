# Print all element of given 2D arrya
nums = [[1,2,3],[4,5,6],[7,8,9]]
rows = len(nums)
cols = len(nums[0])

for i in range(rows):
    for j in range(cols):
        print(nums[i][j],end=" ")
    print()