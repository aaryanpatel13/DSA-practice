"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
 
"""

                                        # BRUTE FORCE APPROACH
                                        # Time Complexity: O
def setZeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    def setInfinity(matrix,row,col):
        
        # Marking the columns
        for i in range(rows):
            if matrix[i][col] != 0:
                matrix[i][col] = float("-INF")
                
        # marking the rows
        for i in range(cols):
            if matrix[row][i] != 0:
                matrix[row][i] = float("-INF")

    
    # Marking infinity    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                setInfinity(matrix,i,j)
    
    # Marking Zeros 
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == float("-INF"):
                matrix[i][j] = 0
        
# TEST CASE

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeros(matrix)
print(matrix)




                                # BETTER APPROACH
                                # Time Complexity: O(N*M)
def setZeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    

    row_track = [0 for _ in range(rows)] #[0] * rows
    col_track = [0 for _ in range(cols)] #[0] * cols
    
    # Tracking in which row or column '0' is present     
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_track[i] = -1
                col_track[j] = -1
                
    # Setting matrix to zero
    for i in range(rows):
        for j in range(cols):
            if row_track[i] == -1 or col_track[j] == -1:
                matrix[i][j] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeros(matrix)
print(matrix)