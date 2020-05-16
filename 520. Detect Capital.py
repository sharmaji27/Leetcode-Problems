'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
 

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        x=[]

        for w in word:
            x.append(w.isupper())

        if sum(x)==len(word) or x[0]==True and sum(x[1:])==0 or sum(x)==0 and True not in x:
            return(True)
        else:
            return(False)