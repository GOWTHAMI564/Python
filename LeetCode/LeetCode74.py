'''74. Search a 2D Matrix'''

'''Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true'''

def searchMatrix(matrix,target) :
    n=len(matrix) # number of rows
    m=len(matrix[0]) # number of columns
    row=0
    col=m-1
    while(row<n and col>=0):
        if(matrix[row][col]==target):
            return True
        elif(target>matrix[row][col]):
            row+=1
        elif(target<matrix[row][col]):
            col-=1
    return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

print(searchMatrix(matrix,target))