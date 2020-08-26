'''
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2 .
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==1:
            return 1
        l=0
        r=n//2 + 1
        while l<=r:
            m = l+(r-l)//2
            x = (m*(m+1)//2)
            if x==n:
                return(m)
            elif x<n:
                l = m+1
            else:
                r=m-1
        return(l-1)