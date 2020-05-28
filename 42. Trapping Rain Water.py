'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
class Solution:
    def trap(self, A: List[int]) -> int:
        water = 0
        left = 0
        right = len(A)-1

        left_biggest_wall = 0
        right_biggest_wall = 0

        while left < right:
            if A[left] < A[right]:
                left_biggest_wall = max(left_biggest_wall,A[left])
                if A[left] < left_biggest_wall:
                    water += left_biggest_wall-A[left]
                left +=1

            else:
                right_biggest_wall = max(right_biggest_wall,A[right])
                if A[right] < right_biggest_wall:
                    water += right_biggest_wall-A[right]
                right-=1

        return(water)