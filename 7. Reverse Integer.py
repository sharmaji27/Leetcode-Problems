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
    def intToRoman(self, num: int) -> str:
        out=''
        I = ['','I','II','III','IV','V','VI','VII','VIII','IX','X']
        X = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC','C']
        C = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM','M']
        M = ['','M','MM','MMM']
        out = M[num//1000]+C[(num%1000)//100]+X[(num%100)//10]+I[num%10]       
        return out.strip()