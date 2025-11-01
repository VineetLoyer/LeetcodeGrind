class Solution:
    def totalMoney(self, n: int) -> int:
        WC = n // 7
        RC = n % 7
        # Full weeks sum: arithmetic series sum for repeated weeks
        # Each week: sum = 7 * (week start value) + sum(0...6) = 7*(i+1) + 21
        Sum = (WC * 28) + (7 * WC * (WC-1) // 2)  # 28 for first week, then increment

        # Leftover days: arithmetic sequence starting from WC+1, length RC
        Sum += (RC * (2*(WC+1) + (RC-1))) // 2  # d=1

        return Sum
