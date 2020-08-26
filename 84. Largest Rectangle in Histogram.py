'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10
'''
class Solution:
    def largestRectangleArea(self, A: List[int]) -> int:
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