'''
Given a 32-bit signed integer, reverse digits of an integer.
Example 1:
Input: 123
Output: 321
Example 2:
Input: -123
Output: -321
Example 3:
Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 
32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        n=0
        if x<0:
            n=1
            x=abs(x)
        while x>0:
            rem = x%10
            rev = rev*10 + rem
            x = x//10
        
        if rev in range(-2**31,2**31):
            if n==1:
                return -1*rev
            else:
                return rev
        else:
            return 0
