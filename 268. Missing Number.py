'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = max(nums)
        s1 = sum(nums)
        s2 = n*(n+1)//2
        if 0 not in nums:
            return 0
        elif s1==s2:
            return n+1
        else:
            return (s2 - s1)