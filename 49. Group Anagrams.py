'''
Given an array of strings, group anagrams together.
Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
All inputs will be in lowercase.
The order of your output does not matter.
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        result = []

        for i in strs:
            if str(sorted(i)) in d:
                d[str(sorted(i))].append(i)
            else:
                d[str(sorted(i))]=[i]

        for i in d:
            result.append(d[i])

        return result