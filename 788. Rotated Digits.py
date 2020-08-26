'''
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].
'''
class Solution:
    def rotatedDigits(self, N: int) -> int:
        d = {'0':'0' , '1':'1' , '2':'5' , '8':'8' , '5':'2' , '6':'9' , '9':'6' }
        def checker(n):
            k=''
            for i in str(n):
                if i not in d.keys():
                    return False
                else:
                    k+=d[i]
            if k!=str(n):
                return True
            else:
                return False
        l=0
        for i in range(N+1):
            if checker(i):
                l+=1
        return l