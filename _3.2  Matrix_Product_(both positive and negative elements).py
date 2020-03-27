# Given a matrix, find the path from top left to bottom right with the greatest
# product by moving only down and right. Print only value.

a = [[-1,2,3],
     [4,5,-6],
     [7,8,9]]

rows = len(a)
columns = len(a[0])
path = [a[0][0]]

dp_matrix_max = [[1 for _ in range (columns)] for k in range(rows)]
dp_matrix_min = [[1 for _ in range (columns)] for k in range(rows)]

for i in range(rows):
    for j in range(columns):
        
        # for first element
        if i==0 and j==0:
            dp_matrix_max[0][0] = a[0][0]
            dp_matrix_min[0][0] = a[0][0]
            
        # for first row
        elif i==0 and j!=0:
            dp_matrix_max[i][j] = a[i][j]*dp_matrix_max[i][j-1]
            dp_matrix_min[i][j] = a[i][j]*dp_matrix_min[i][j-1]
            
        # for first column
        elif j==0 and i!=0:
            dp_matrix_max[i][j] = dp_matrix_max[i-1][j]*a[i][j]
            dp_matrix_min[i][j] = dp_matrix_min[i-1][j]*a[i][j]
            
        # for inner elements
        elif i!=0 and j!=0:
            if a[i][j] < 0:
                dp_matrix_max[i][j] = max(a[i][j]*dp_matrix_max[i-1][j] , a[i][j]*dp_matrix_max[i][j-1],a[i][j]*dp_matrix_min[i-1][j] , a[i][j]*dp_matrix_min[i][j-1])
                dp_matrix_min[i][j] = max(a[i][j]*dp_matrix_max[i-1][j] , a[i][j]*dp_matrix_max[i][j-1],a[i][j]*dp_matrix_min[i-1][j] , a[i][j]*dp_matrix_min[i][j-1])
 
            else:
                dp_matrix_max[i][j] = max(a[i][j]*dp_matrix_max[i-1][j] , a[i][j]*dp_matrix_max[i][j-1])
                dp_matrix_min[i][j] = min(a[i][j]*dp_matrix_min[i-1][j] , a[i][j]*dp_matrix_min[i][j-1])
                                
print (dp_matrix_max[-1][-1])
