class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs:
            return 0
        rows,cols = len(strs),len(strs[0])
        deletion = 0
        for c in range(cols):
            for r in range(1,rows):
                if strs[r][c]<strs[r-1][c]:
                    deletion+=1
                    break
        return deletion