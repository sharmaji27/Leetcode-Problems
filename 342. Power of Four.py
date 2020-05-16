'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n>0:
            if n==1:
                return(True)
            elif n%4==0:
                n/=4
            else:
                return False
        return(False)