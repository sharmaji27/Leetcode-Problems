'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=0
        r=num
        while l<=r:
            m = l+(r-l)//2
            if m*m == num:
                return True
                break
            elif m*m < num:
                l = m+1
            else:
                r= m-1
        return False 