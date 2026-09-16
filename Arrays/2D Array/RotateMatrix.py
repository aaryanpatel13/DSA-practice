"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

"""

#                           BRUTE OFRCE APPROACH


#                           Time Complexity: O(N²)
#                          Space Complexity: O(N²)

def rotateMatrix(matrix):
    # rows = len(matrix)
    # cols = len(matrix[0])
    n = len(matrix)
    
    res = [[0 for _  in range (n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            res[j][n-1-i] = matrix[i][j]
    return res
        
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotateMatrix(matrix))



#                           OPTIMAL SOLUTION [We change the matrix itself without taking any extra space]
#                           Time Complexity: O(N²)
#                          Space Complexity: O(1)

def rotateMatrix(matrix):
    n = len(matrix)
    
    #Transposing the matrix
    for i in range(n-1):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reversing the each row of given matrix
    for i in range(n):
        matrix[i].reverse()
    print(matrix)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotateMatrix(matrix)



    