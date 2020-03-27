# Question: Given an n x m array where all rows and columns are in sorted order, write a
# function to determine whether the array contains an element x.


matrix = [[0,1,2,3],
          [4,5,6,7],
          [8,9,10,11],
          [12,13,15,16]]

x = 14
flag=0

rows = len(matrix)
cols = len(matrix[0])


if x<matrix[0][0]:
    print(False)
    

for r in range(rows):
    if x <= matrix[r][-1]:
        while 1:
            if matrix[r][cols-1] == x:
                flag=1
                print(r,cols-1)
                break
            
            elif matrix[r][cols-1] > x:
                cols = cols-1
            
            else: 
                break
                
print([False,True][flag])