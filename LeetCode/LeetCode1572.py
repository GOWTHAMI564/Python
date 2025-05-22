'''1572. Matrix Diagonal Sum'''
'''
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
'''


def diagonalSum(mat) :
    n=len(mat)
    res=0
    mid=n//2
    for i in range(n):
        res+=mat[i][i]+mat[i][n-1-i]
    if n%2 == 1:
        res-=mat[mid][mid] 
    return res
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
print(diagonalSum(mat))