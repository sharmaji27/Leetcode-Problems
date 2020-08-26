'''
Given a string containing just the characters '(' and ')', find the length of the longest 
valid (well-formed) parentheses substring.
Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for p in range(len(s)):
            if s[p] == '(':
                stack.append(p)
            else:
                stack.pop()
                if stack == []:
                    stack.append(p)
                else:
                    max_len = max(p-stack[-1],max_len)
        return(max_len)