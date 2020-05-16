class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        r,c,neg_count = 0,n-1,0

        while r<m and c>=0:
            if grid [r][c]<0:
                neg_count = neg_count + m-r
                c-=1
            else:
                r+=1
        return (neg_count)