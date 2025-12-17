class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if k <= 0 or n < 2:
            return 0
        if k >= n - 1:
            return sum(abs(prices[i] - prices[i - 1]) for i in range(1, n))
        NEG = -10**18
        dp0 = [NEG] * (k + 1)
        dpL = [NEG] * (k + 1)
        dpS = [NEG] * (k + 1)
        dp0[0] = 0
        for p in prices:
            new0 = dp0[:]
            newL = dpL[:]
            newS = dpS[:]
            for t in range(k + 1):
                if dp0[t] != NEG:
                    if dp0[t] - p > newL[t]:
                        newL[t] = dp0[t] - p
                    if dp0[t] + p > newS[t]:
                        newS[t] = dp0[t] + p
                if t + 1 <= k:
                    if dpL[t] != NEG and dpL[t] + p > new0[t + 1]:
                        new0[t + 1] = dpL[t] + p
                    if dpS[t] != NEG and dpS[t] - p > new0[t + 1]:
                        new0[t + 1] = dpS[t] - p
            dp0, dpL, dpS = new0, newL, newS
        return max(dp0)