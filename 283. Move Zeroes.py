'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        
        def find_z(start):
            for i in range(start,l):
                if nums[i]==0:
                    return i

        def find_nz(start):
            for i in range(start,l):
                if nums[i]!=0:    
                    return i

        start=0

        if set(nums)=={0}:
            pass
        elif 0 not in nums:
            pass
        else:
            while 1:
                fz = find_z(start)
                fnz = find_nz(fz)
                if sum(nums[fz:])==0:
                    break
                nums[fz],nums[fnz] = nums[fnz],nums[fz]
                start= fz + 1
                if sum(nums[start:])==0:
                    break
