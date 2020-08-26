class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        if len(s)<1:
            return 0
        elif s==' ':
            return 1
        c=0
        m=0
        for i in range(len(s)):
            if ord(s[i]) not in d:
                d[ord(s[i])] = i
                c=c+1
            else:
                if i-c > d[ord(s[i])]:
                    c=c+1
                else:
                    c=i-d[ord(s[i])]    
                d[ord(s[i])] = i
            
            if c>m:
                m=c
        if c>m:
            return c
        else:
            return m