class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0]*n for _ in range(m)]
        for r,c in walls:
            grid[r][c]=1
        for r,c in guards:
            grid[r][c]=2
        
        for gr,gc in guards:
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr,nc = gr+dr,gc+dc
                while 0<=nr<m and 0<=nc<n and grid[nr][nc]!=1 and grid[nr][nc]!=2:
                    if grid[nr][nc]==0:
                        grid[nr][nc]=3
                    nr+=dr
                    nc+=dc
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    ans+=1
        return ans