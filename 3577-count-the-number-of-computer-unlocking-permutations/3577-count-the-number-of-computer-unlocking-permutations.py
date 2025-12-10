MOD = 10**9 + 7
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        root = complexity[0]

        # Step 1: check feasibility
        for i in range(1, n):
            if complexity[i] <= root:
                return 0

        # Step 2: compute (n-1)! mod MOD
        ans = 1
        for k in range(1, n):
            ans = ans * k % MOD
        return ans