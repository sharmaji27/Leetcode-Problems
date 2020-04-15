'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

'''

# ITERATIVE
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        
        if n==1:
            return x
        
        if x==0:
            return 0
        
        if x==1:
            return 1
        
        if n<0:
            x = 1/x
            n=-n
        
        
        y=1
        
        while n>0:
            if n%2:
                y = y*x
                
            x*=x
            n//=2

        return y
    
# RECURSIVE
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        
        if n==1:
            return x
        
        if x==0:
            return 0
        
        if x==1:
            return 1
        
        if n<0:
            return 1/self.myPow(x,-n)
        
        if n%2:
            return x*self.myPow(x,n-1)
        else:
            return self.myPow(x*x, n//2)
        
# DIRECT
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n