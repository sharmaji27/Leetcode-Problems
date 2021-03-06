'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

'''

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        res = 0
        while left <= right:
            mid = (right + left) // 2
            if mid * mid <= x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res