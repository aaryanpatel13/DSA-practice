# Print both diagonals of given 2D list
nums = [[10,25,30],[7,12,5],[9,0,18]] 
#Diagonal1: 10 12 18
#Diagonal2: 3 12 9

rows = len(nums)
cols = len(nums[0])

print("Diagonal1: ", end="")
for i in range(rows):
    print(nums[i][i],end=" ")

print()

print("Diagonal2: ",end="")
for i in range(rows):
    print(nums[i][cols-1-i],end=" ")
print()