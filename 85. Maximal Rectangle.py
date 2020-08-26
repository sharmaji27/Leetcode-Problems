'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''
class Solution:
    def maximalRectangle(self, rect: List[List[str]]) -> int:
        def largestRectangleArea(A):
            stack = []
            maxi = 0
            i = 0
            while i<len(A):
                if len(stack)==0 or A[stack[-1]]<=A[i]:
                    stack.append(i)
                    i+=1
                else:
                    top = stack.pop()
                    if len(stack)==0:
                        ar = A[top]*(i)
                    else:
                        ar = A[top]*(i-stack[-1]-1)
                    maxi = max(maxi,ar)
        
            while len(stack)!=0:
                top = stack.pop()
                if len(stack)==0:
                    ar = A[top]*(i)
                else:
                    ar = A[top]*(i-stack[-1]-1)
                maxi = max(maxi,ar)
        
            return(maxi)
        
        
        if rect==[]:return 0
        rows = len(rect)
        cols = len(rect[0])
        for i in range(rows):
            for j in range(cols):
                rect[i][j] = int(rect[i][j])
        
    
        m = largestRectangleArea(rect[0])

        
        
        for i in range(1,rows):
            for j in range(cols):
                if rect[i][j]==1:
                    rect[i][j] = rect[i-1][j]+1
            m = max(m,largestRectangleArea(rect[i]))
        
        return (m)