class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        half = k // 2

        # Base profit with original strategy
        base = 0
        for p, s in zip(prices, strategy):
            base += p * s

        # If we apply no modification
        ans = base

        # Initial window [0 .. k-1]
        old = 0  # sum(strategy[i] * prices[i]) over current k-window
        for i in range(k):
            old += strategy[i] * prices[i]

        sell = 0  # sum(prices[i]) over the last half of the current window
        for i in range(half, k):
            sell += prices[i]

        ans = max(ans, base - old + sell)

        # Slide window start l from 1 to n-k
        for l in range(1, n - k + 1):
            # update old window contribution
            old -= strategy[l - 1] * prices[l - 1]
            old += strategy[l + k - 1] * prices[l + k - 1]

            # update sell-half sum: [l+half .. l+k-1]
            sell -= prices[l - 1 + half]
            sell += prices[l + k - 1]

            ans = max(ans, base - old + sell)

        return ans