'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true

'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        boo = True

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif ch in ')]}':
                try:
                    popped_element = stack.pop()
                except:
                    boo=False
                    break
                if popped_element=='(' and ch==')':
                    pass
                elif popped_element=='{' and ch=='}':
                    pass
                elif popped_element=='[' and ch==']':
                    pass
                else:
                    boo=False
                    break
        if len(stack)==0:
            return (boo)
        else:
            return (False)