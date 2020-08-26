class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            print(nums[0])

        global_max = nums[0]
        current_sum = nums[0]

        for i in range(1,len(nums)):
            current_sum = max(current_sum+nums[i],nums[i])
            global_max = max(current_sum,global_max)

        return global_max