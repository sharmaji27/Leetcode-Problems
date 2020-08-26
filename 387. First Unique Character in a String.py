'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1

        for k,v in d.items():
            if v==1:
                return s.index(k)
        return -1