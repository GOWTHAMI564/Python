'''48. Rotate Image'''
'''Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]'''


def rotate(matrix) :
    """
    Do not return anything, modify matrix in-place instead.
    """
    n=len(matrix)
    m=len(matrix[0])
    dupMat=[]
    for i in range(n):
        temp=[0]*n
        dupMat.append(temp)
    for i in range(0,n):
        for j in range(0,n):
            dupMat[j][n-i-1]=matrix[i][j]
    for i in range(0,n):
        for j in range(0,n):
            matrix[i][j]=dupMat[i][j]
    return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))


''' TC : O(N2)  SC = O(n2) [ since we are using extra extra matrix (dupMat)]'''

# OPTIMAL CODE USING TRANSPOSE AND REVERSE ROWS

def rotate(matrix) :
    """
    Do not return anything, modify matrix in-place instead.
    """
    n=len(matrix)
    for i in range(n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j] 
    for i in range(n):
        matrix[i]=matrix[i][::-1]
    return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))