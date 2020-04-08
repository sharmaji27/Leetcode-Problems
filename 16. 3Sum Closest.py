class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = nums[0] + nums[1] + nums[2]
        nums.sort()
        
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(target - total) < abs(target - closest):
                    closest = total
                    
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return closest
                
        return closest 