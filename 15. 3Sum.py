'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        l=[]
        for j in range(len(nums)):
            target = 0-nums[j]
            d={}
            for i in range(j+1,len(nums)):
                if nums[i] in d:
                    l.append((nums[j],nums[d[nums[i]]],nums[i]))
                else:
                    d[target-nums[i]] = i
        l=set(l)
        l=[list(a) for a in l]
        return l