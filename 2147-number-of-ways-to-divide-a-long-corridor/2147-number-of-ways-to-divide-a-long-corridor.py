class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1_000_000_007
        seats = [i for i, ch in enumerate(corridor) if ch == 'S']
        m = len(seats)
        if m == 0 or m % 2 == 1:
            return 0

        ways = 1
        # multiply choices between consecutive seat-pairs
        for k in range(1, m // 2):
            ways = (ways * (seats[2*k] - seats[2*k - 1])) % MOD
        return ways