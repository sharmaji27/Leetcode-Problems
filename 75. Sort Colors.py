'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
'''
class Solution:
    def sortColors(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(A)-1
        scan = 0
        
        while scan<=r:
            if A[scan]==0:
                A[scan],A[l] = A[l],A[scan]
                l+=1
                scan+=1
            elif A[scan]==2:
                A[scan],A[r] = A[r],A[scan]
                r-=1
            else:
                scan+=1
        return(A)