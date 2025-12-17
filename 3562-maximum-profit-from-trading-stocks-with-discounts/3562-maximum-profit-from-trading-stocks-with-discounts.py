class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        def to_one_based(a: List[int]) -> List[int]:
            if len(a) == n + 1:
                return a
            if len(a) == n:
                return [0] + a
            if len(a) < n + 1:
                return [0] + a + [0] * (n - len(a))
            return a

        P = to_one_based(present)
        F = to_one_based(future)
        children = [[] for _ in range(n + 1)]
        indeg = [0] * (n + 1)
        for u, v in hierarchy:
            children[u].append(v)
            indeg[v] += 1
        root = next((i for i in range(1, n + 1) if indeg[i] == 0), 1)
        NEG = -10**18

        def merge(base, add):
            new = [NEG] * (budget + 1)
            for b in range(budget + 1):
                if base[b] == NEG:
                    continue
                rem = budget - b
                row = add
                for k in range(rem + 1):
                    if row[k] == NEG:
                        continue
                    val = base[b] + row[k]
                    if val > new[b + k]:
                        new[b + k] = val
            return new

        dp = [None] * (n + 1)

        def dfs(u: int):
            for v in children[u]:
                dfs(v)
            dp_skip = [0] + [NEG] * budget
            for v in children[u]:
                dp_skip = merge(dp_skip, dp[v][0])

            def build_buy(parent_bought: int):
                price = P[u] if parent_bought == 0 else (P[u] // 2)
                gain = F[u] - price
                buy = [NEG] * (budget + 1)
                if price <= budget:
                    buy[price] = gain
                for v in children[u]:
                    buy = merge(buy, dp[v][1])
                return buy

            buy0 = build_buy(0)
            buy1 = build_buy(1)
            dp0 = [max(a, b) for a, b in zip(dp_skip, buy0)]
            dp1 = [max(a, b) for a, b in zip(dp_skip, buy1)]
            dp[u] = (dp0, dp1)

        dfs(root)
        return max(0, max(dp[root][0]))