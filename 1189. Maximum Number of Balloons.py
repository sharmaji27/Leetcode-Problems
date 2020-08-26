'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.
'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d={}
        s='balloon'
        for i in text:
            if i in s:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1

        c=0
        while(d.get('b',0)>=1 and d.get('a',0)>=1 and d.get('l',0)>=2 and d.get('o',0)>=2 and d.get('n',0)>=1):
            c+=1
            d['b']-=1
            d['a']-=1
            d['l']-=2
            d['o']-=2
            d['n']-=1

        return c
        
#######################################################################

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c=collections.Counter(text)
        return min(c['b'],c['a'],c['l']//2,c['o']//2,c['n'])