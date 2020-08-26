'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:


'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        wall_sharing = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    res+=1
        
                    if i!=0 and grid[i-1][j]==1:
                        wall_sharing+=1

                    if j!=0 and grid[i][j-1]==1:
                        wall_sharing+=1

        return ((4*res)-(2*wall_sharing))