'''
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not 
part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        if l==0:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+l]==needle:
                return i

        return -1