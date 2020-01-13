class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        l = len(needle)
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                if haystack[i:i+l]==needle:
                    return i
                
        return -1