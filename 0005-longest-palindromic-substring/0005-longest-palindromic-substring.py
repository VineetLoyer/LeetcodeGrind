class Solution:
    def longestPalindrome(self, s: str) -> str:
        # resIdx, resLen = 0, 0
        # n = len(s)

        # dp = [[False] * n for _ in range(n)]

        # for i in range(n - 1, -1, -1):
        #     for j in range(i, n):
        #         if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
        #             dp[i][j] = True
        #             if resLen < (j - i + 1):
        #                 resIdx = i
        #                 resLen = j - i + 1

        # return s[resIdx : resIdx + resLen]

        #use expand around center technique instead of DP as DP table takes O(n^2) time.
        n = len(s)
        if n<=1:
            return s
        start,best_len = 0,1
        def expand(l:int,r:int)->None:
            nonlocal start,best_len
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            curLen = r-(l+1)
            if curLen > best_len:
                best_len = curLen
                start = l+1
        for i in range(n):
            expand(i,i)
            expand(i,i+1)
        return s[start: start + best_len]