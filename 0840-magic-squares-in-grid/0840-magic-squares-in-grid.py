class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        # Helper function to check if a 3x3 grid starting at (r, c) is a magic square
        def isMagic(r, c):
            # Optimization: The center of a 1-9 magic square must be 5
            if grid[r+1][c+1] != 5:
                return False
            
            # 1. Check if numbers 1-9 are present and distinct
            # We collect all 9 numbers in the subgrid
            vals = []
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    val = grid[i][j]
                    if val < 1 or val > 9: # Must be within 1-9
                        return False 
                    vals.append(val)
            
            if len(set(vals)) != 9: # Must be distinct
                return False
            
            # 2. Check Sums (Target sum for 1-9 magic square is always 15)
            # Row sums
            if (grid[r][c] + grid[r][c+1] + grid[r][c+2] != 15 or
                grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] != 15 or
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != 15):
                return False
            
            # Column sums
            if (grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15 or
                grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15 or
                grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15):
                return False
                
            # Diagonal sums
            if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15):
                return False
                
            return True

        # Iterate over all possible top-left corners of 3x3 grids
        for r in range(rows - 2):
            for c in range(cols - 2):
                if isMagic(r, c):
                    count += 1
                    
        return count