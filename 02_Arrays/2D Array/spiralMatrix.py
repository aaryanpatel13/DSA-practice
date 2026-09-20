"""
Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

"""
#                                  Optimal Solution

def spiralMatrix(matrix):
    if not matrix or not matrix[0]:
        return []

    ans = []
    left , top = 0,0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1
    

    while left <= right and top <= bottom:
        # step 1: Move left to right
        for i in range(left,right+1):
            ans.append(matrix[top][i])
        top += 1

        # step 2: move top to bottom
        for i in range(top,bottom+1):
            ans.append(matrix[i][right])
        right -= 1
        
        #step 3: move right to left if left <= right
        if top <= bottom: # Incsse only ONE row is there
            for i in range(right,left-1,-1):
                ans.append(matrix[bottom][i])
            bottom -= 1
        
        #step 4: move bottom to top is top <= bottom
        if left <= right: # Incase only ONE column is there
            for i in range(bottom,top-1,-1):
                ans.append(matrix[i][left])
            left += 1
    return ans
    


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralMatrix(matrix))