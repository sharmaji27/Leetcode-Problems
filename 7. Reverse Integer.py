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