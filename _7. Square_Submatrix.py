# Given a 2D array of 1s and 0s, find the largest square subarray of all 1s.

a = [[1,1,1,0],
     [1,1,1,1],
     [1,1,0,1]]

rows = len(a)
cols = len(a[0])
m= 0 
flag = 0

dp_matrix = [[0 for _ in range (cols)] for k in range (rows)]

for i in range(rows):
    for j in range(cols):
        
        # checking if 1 exist in matrix or not
        if flag==0 and a[i][j]==1:
            flag=1
        
        # first row and first column
        if i==0 or j==0 :
            dp_matrix[i][j] = a[i][j]
        
        elif  i==j and dp_matrix[i-1][j]==1 and dp_matrix[i][j-1]==1 and dp_matrix[i-1][j-1]!=0 and a[i][j]!=0:
            dp_matrix[i][j] = a[i][j] + dp_matrix[i-1][j-1]
            if dp_matrix[i][j]>m:
                m= dp_matrix[i][j]
        
        else:
            dp_matrix[i][j] = a[i][j]
            
if flag==1:
    print([m,1][1>m])
else:
    print(m)