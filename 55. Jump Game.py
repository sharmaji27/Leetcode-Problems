'''

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = 0
        curr_end = 0
        curr_max = 0
        flag=0
        if len(nums)==1:
            return True

        for i in range(len(nums)):
            curr_max = max(curr_max,i+nums[i])
            if i == curr_end:
                jumps+=1
                curr_end = curr_max
                if curr_end>=len(nums)-1:
                    flag=1

        return ([True,False][flag==0])