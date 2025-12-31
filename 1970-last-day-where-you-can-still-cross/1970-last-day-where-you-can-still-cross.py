from collections import deque
from typing import List

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        # Helper function to check if a path exists on a specific day
        def canCross(day: int) -> bool:
            # 1. Create a grid for the current state
            # 0 = Land, 1 = Water
            grid = [[0] * col for _ in range(row)]
            
            # 2. Mark the cells as water for all days up to the current 'day'
            # Note: We iterate through the first 'day' number of cells
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1  # Convert 1-based input to 0-based index
            
            # 3. BFS Setup
            queue = deque()
            visited = set()
            
            # Add all land cells from the TOP ROW (row 0) to the queue
            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    visited.add((0, c))
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            while queue:
                r, c = queue.popleft()
                
                # If we reached the bottom row, path exists
                if r == row - 1:
                    return True
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check bounds, if it's land (0), and not visited
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        
            return False

        # Binary Search for the last possible day
        left, right = 1, len(cells)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canCross(mid):
                ans = mid      # If we can cross on day 'mid', try a later day
                left = mid + 1
            else:
                right = mid - 1 # If we can't, try an earlier day
                
        return ans