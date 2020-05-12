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
        if len(s)!=len(t):
            return (False)
        else:
            d1={}
            d2={}
            for i in range(len(s)):
                if s[i] not in d1:
                    d1[s[i]]=1
                else:
                    d1[s[i]]+=1

            for i in range(len(t)):
                if t[i] not in d2:
                    d2[t[i]]=1
                else:
                    d2[t[i]]+=1
            return(d1==d2)