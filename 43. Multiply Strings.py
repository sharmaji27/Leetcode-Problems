'''

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Note:

1.The length of both num1 and num2 is < 110.
2.Both num1 and num2 contain only digits 0-9.
3.Both num1 and num2 do not contain any leading zero, except the number 0 itself.
4.You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

        n1=0
        n2=0

        for i in num1:
            n1 = n1*10 + d[i]

        for i in num2:
            n2 = n2*10 + d[i]

        return str(n1*n2)