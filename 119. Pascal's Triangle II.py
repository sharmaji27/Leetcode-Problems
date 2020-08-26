'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
'''
class Solution:
    def getRow(self, n: int) -> List[int]:
        res = [[1],[1,1],[1,2,1]]
        if n<3:
            return(res[n])
        else:
            n=n+1
            for i in range(3,n):
                a=[1]
                if i%2==0:
                    for j in range(i//2):
                        a.append(res[-1][j] + res[-1][j+1])
                    re = a+a[::-1][1:]
                else:
                    for j in range((i//2)+1):
                        a.append(res[-1][j] + res[-1][j+1])
                    re = a+a[::-1][2:]
                res.append(re)
            return res[-1]