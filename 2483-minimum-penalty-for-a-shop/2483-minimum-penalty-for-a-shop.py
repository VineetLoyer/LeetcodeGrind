class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        # prefixY[i] = number of 'Y' in customers[0:i]
        prefixY = [0] * (n + 1)
        for i, c in enumerate(customers, 1):
            prefixY[i] = prefixY[i - 1] + (1 if customers[i - 1] == 'Y' else 0)

        totalY = prefixY[n]

        best_hour = 0
        min_penalty = float('inf')

        # Try closing at every hour j from 0..n
        for j in range(n + 1):
            # 'N' during open hours [0, j-1]
            open_no_cust = j - prefixY[j]

            # 'Y' during closed hours [j, n-1]
            closed_with_cust = totalY - prefixY[j]

            penalty = open_no_cust + closed_with_cust

            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = j  # earliest hour with this minimal penalty

        return best_hour