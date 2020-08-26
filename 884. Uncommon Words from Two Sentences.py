'''
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
 

Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
'''
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        d={}

        for i in A.split():
            d[i] = d.get(i, 0) + 1

        for i in B.split():
            d[i] = d.get(i, 0) + 1

        l=[]
        for k,v in d.items():
            if v==1:
                l.append(k)

        return(l)