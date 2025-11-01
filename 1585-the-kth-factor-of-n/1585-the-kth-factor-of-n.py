class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        large_factors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    large_factors.append(n // i)
        # Combine factors in correct order: small factors first, then reversed large factors
        all_factors = factors + large_factors[::-1]
        return all_factors[k-1] if k <= len(all_factors) else -1
        