class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base case for n = 1
        # Type ABA: 3 choices for 1st, 2 for 2nd, 3rd is fixed to 1st (3 * 2 * 1 = 6)
        aba = 6
        # Type ABC: 3 choices for 1st, 2 for 2nd, 1 for 3rd (3 * 2 * 1 = 6)
        abc = 6
        
        # Iterate from the 2nd row up to n
        for _ in range(n - 1):
            # Calculate new counts based on transition rules
            new_aba = (3 * aba + 2 * abc) % MOD
            new_abc = (2 * aba + 2 * abc) % MOD
            
            # Update current counts
            aba, abc = new_aba, new_abc
            
        return (aba + abc) % MOD