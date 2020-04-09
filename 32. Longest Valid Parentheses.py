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