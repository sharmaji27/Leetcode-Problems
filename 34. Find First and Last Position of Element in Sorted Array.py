class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        i = 0
        j = l-1
        
        if l==0:
            return [-1,-1]
        
        while(i<j):
            mid = i + (j-i)//2
            if nums[mid]<target:
                i = mid+1
            else:
                j = mid

        if nums[i]!=target:
            return [-1,-1]
        start=i
        
        j=l-1
        while(i<j):
            mid = i + (j-i)//2 + 1
            if nums[mid]>target:
                j = mid-1
            else:
                i = mid
        end=i
        return [start,end]