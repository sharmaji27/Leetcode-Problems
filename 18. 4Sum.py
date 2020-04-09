'''
Given an array nums of n integers and an integer target, are there elements a, b, c, 
and d in nums such that a + b + c + d = target? Find all unique quadruplets in the 
array which gives the sum of target.
Note:
The solution set must not contain duplicate quadruplets.
Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            t1 = target-nums[i]

            for j in range(i+1,len(nums)):

                #two sum starts form here        
                t2 = t1-nums[j]
                ht = {}
                for k in range(j+1,len(nums)):
                    if nums[k] in ht:
                        if [nums[i],nums[j],nums[k],t2-nums[k]] not in result:
                            result.append([nums[i],nums[j],nums[k],t2-nums[k]])
                    else:
                         ht[t2-nums[k]] = k
        return result

