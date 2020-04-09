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

