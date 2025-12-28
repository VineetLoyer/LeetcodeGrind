class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]<0:
                    count+=1
        return count