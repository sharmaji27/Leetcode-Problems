'''
Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

'''

class Solution:
    def isPalindrome(self, x: int) -> bool:        
        def reverse(n):
            rev=0
            while n!=0:
                rem = n%10
                rev=rev*10+rem
                n=n//10
            return rev

        if x<0:
            return False
        else:
            return x==reverse(x)
        