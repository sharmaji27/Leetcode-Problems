'''
Given an unsorted integer array, find the smallest missing positive integer.
Example 1:
Input: [1,2,0]
Output: 3
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d = {}
        l = len(nums)
        if nums == []:
            return 1
        if nums==[1]:
            return 2
        
        for i in range(l):
            if i==1:
                one_present = True
            d[nums[i]] = i
        
        for i in range(1,l+1):
            if i not in d:
                if i==None:
                    break
                else:
                    return i
        return l+1