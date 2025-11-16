class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        current = 0

        for c in s:
            if c == '1':
                current += 1
            else:
                ans = (ans + current * (current + 1) // 2) % MOD
                current = 0
        ans = (ans + current * (current + 1) // 2) % MOD
        return ans