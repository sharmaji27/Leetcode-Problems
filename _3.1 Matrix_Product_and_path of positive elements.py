# Given a matrix, find the path from top left to bottom right with the greatest
# product by moving only down and right.

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

rows = len(a)
columns = len(a[0])
path = [a[0][0]]

dp_matrix = [[1 for _ in range (columns)] for k in range(rows)]

for i in range(rows):
    for j in range(columns):
        
        # for first element
        if i==0 and j==0:
            dp_matrix[0][0] = a[0][0]
            
        # for first row
        elif i==0 and j!=0:
            dp_matrix[i][j] = a[i][j]*dp_matrix[i][j-1]
            
        # for first column
        elif j==0 and i!=0:
            dp_matrix[i][j] = dp_matrix[i-1][j]*a[i][j]
            
        # for inner elements
        elif i!=0 and j!=0:
            dp_matrix[i][j] = max(a[i][j]*dp_matrix[i-1][j] , a[i][j]*dp_matrix[i][j-1])

# for path
i=0
j=0

while 1:
    
    # break if bottom right is reached
    if i==rows-1 and j==columns-1:
        break
    
    # move right if u r on the bottom left
    elif i==rows-1 and j!=columns-1:
        j+=1
        path.append(a[i][j])
    
    # move down if u r in the top right
    elif i!=rows-1 and j==columns-1:
        i+=1
        path.append(a[i][j])    
    
    # general cases for inner elements
    elif dp_matrix[i+1][j] > dp_matrix[i][j+1]:
        i+=1
        path.append(a[i][j])
    
    elif dp_matrix[i+1][j] < dp_matrix[i][j+1]:
        j+=1
        path.append(a[i][j])
    
    
print (path)
print(dp_matrix[-1][-1])