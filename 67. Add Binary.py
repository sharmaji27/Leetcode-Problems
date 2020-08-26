'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m,n,carry = len(a)-1,len(b)-1,0
        res = []
        while m>=0 or n>=0 or carry!=0:
            if m>=0:
                carry += int(a[m])
                m-=1
            if n>=0:
                carry += int(b[n])
                n-=1
            
            res.append(str(carry%2))
            carry //= 2
            
        return ''.join(reversed(res))