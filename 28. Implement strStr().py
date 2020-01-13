class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        if l==0:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+l]==needle:
                return i

        return -1