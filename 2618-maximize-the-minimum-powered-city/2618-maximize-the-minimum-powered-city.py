class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        # 1) Base power per city via prefix sums (sliding window [i-r, i+r])
        pref = [0] * (n + 1)
        for i, x in enumerate(stations):
            pref[i + 1] = pref[i] + x

        def base_power(i: int) -> int:
            L = max(0, i - r)
            R = min(n - 1, i + r)
            return pref[R + 1] - pref[L]

        base = [base_power(i) for i in range(n)]

        # 2) Feasibility check for minimum power X
        def feasible(X: int) -> bool:
            used = 0
            diff = [0] * (n + 1)  # range add diff array over city indices
            add_running = 0       # current extra coverage affecting this index

            for i in range(n):
                add_running += diff[i]
                curr = base[i] + add_running
                if curr < X:
                    need = X - curr
                    used += need
                    if used > k:
                        return False

                    # Place 'need' stations at pos = min(n-1, i+r)
                    pos = min(n - 1, i + r)
                    L = max(0, pos - r)
                    R = min(n - 1, pos + r)

                    # Apply range add [L, R]
                    diff[L] += need
                    if R + 1 < n:
                        diff[R + 1] -= need

                    # Since i ∈ [L, R], it should affect the current city immediately
                    add_running += need

            return True

        # 3) Binary search on the answer
        lo, hi = 0, 10**18
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo