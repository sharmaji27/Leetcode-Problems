'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[[1],[1,1],[1,2,1]]
        if numRows<=3:
            return l[:numRows]
        else:
            for i in range(3,numRows):
                a=[1]
                if i%2==0:
                    for j in range(i//2):
                        a.append(l[-1][j] + l[-1][j+1])
                    l.append(a+a[::-1][1:])
                else:
                    for j in range((i//2)+1):
                        a.append(l[-1][j] + l[-1][j+1])
                    l.append(a+a[::-1][2:])

            return l