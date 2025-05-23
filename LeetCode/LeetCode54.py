''' 54. Spiral Matrix '''
'''Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]'''

def spiralOrder(matrix) :
    n=len(matrix) #total rows
    m=len(matrix[0]) #total cols
    sr=0
    er=n-1
    sc=0
    ec=m-1
    result=[]
    while(sr<=er and sc<=ec):
        #left to right
        for i in range(sc,ec+1):
            result.append(matrix[sr][i])
        sr+=1
        #top to bottom
        for i in range(sr,er+1):
            result.append(matrix[i][ec])
        ec-=1
        if(sr<=er):
            # To check we have other row
            #right to left
            for i in range(ec,sc-1,-1):
                result.append(matrix[er][i])
            er-=1
        if(sc<=ec): 
            # To check for other col
            # then Bottom to top
            for i in range(er,sr-1,-1):
                result.append(matrix[i][sc])
            sc+=1
    return result

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))