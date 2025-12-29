from collections import defaultdict
from functools import lru_cache

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        # Step 1: build mapping
        rules = defaultdict(list)
        for a in allowed:
            rules[(a[0], a[1])].append(a[2])

        @lru_cache(None)
        def dfs(row: str) -> bool:
            # Base case: reached the top
            if len(row) == 1:
                return True

            # Build all possible next rows
            def build_next(index, current):
                if index == len(row) - 1:
                    return dfs(current)

                pair = (row[index], row[index + 1])
                if pair not in rules:
                    return False

                for ch in rules[pair]:
                    if build_next(index + 1, current + ch):
                        return True
                return False

            return build_next(0, "")

        return dfs(bottom)
