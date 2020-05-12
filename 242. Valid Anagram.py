'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = {}

        for i in s:
            if i not in c:
                c[i]=1
            else:
                c[i]+=1

        for i in t:
            if i not in c:
                return( False)
            else:
                c[i]-=1
                if c[i]<0:
                    return( False)

        for v in c.values():
            if v!=0:
                return(False)

        return (True)