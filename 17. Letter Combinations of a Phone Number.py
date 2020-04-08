class Solution:
    def letterCombinations(self,digits):
        digits = str(digits)
        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',                    '8': 'tuv', '9': 'wxyz'}
        res = helper(digits,phone)
        return res

def helper(digits,phone):
    if not digits:
        return []
    if len(digits)==1:
        return list(phone[digits])
    back = helper(digits[1:],phone)
    front = list(phone[digits[0]])
    res = [f+b for f in front  for b in back]
    return res