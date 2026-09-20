#Print the upper triangle part of a given 2D list

nums  = [[10,25,30],
        [7,12,15],
        [9,0,18]]

rows = len(nums) 
cols = len(nums[0])

for i in range(0,rows):
    for j in range(0,cols):
        if j >= i:
            print(nums[i][j],end=" ")
        else:
            print("* ", end= " ")
    print()