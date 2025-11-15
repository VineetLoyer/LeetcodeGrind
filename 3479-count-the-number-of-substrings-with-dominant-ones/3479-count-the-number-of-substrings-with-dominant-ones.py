class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                L = j - i
                ans += L * (L + 1) // 2
                i = j
            else:
                i += 1
        zeros = [idx for idx, ch in enumerate(s) if ch == '0']
        m = len(zeros)
        if m == 0:
            return ans  # all substrings already counted as all-ones

        B = isqrt(n) + 2

        zeros = [-1] + zeros + [n]
        for k in range(1, min(B, m) + 1):
            Lmin = k * k + k  # minimum length for dominant ones with k zeros

            # Slide a window of k consecutive zeros
            for w in range(1, m - k + 2):
                first_zero = zeros[w]
                last_zero = zeros[w + k - 1]
                prev_zero = zeros[w - 1]
                next_zero = zeros[w + k]

                # Start and end ranges
                S1 = prev_zero + 1
                S2 = first_zero
                E1 = last_zero
                E2 = next_zero - 1

                if S1 > S2 or E1 > E2:
                    continue  # no valid substrings for this block

                A = S2 - S1 + 1  # number of possible starts

                # First E that can yield any valid length
                E0 = max(E1, S1 + Lmin - 1)
                if E0 > E2:
                    continue  # even the longest substring is too short

                # Up to where E uses the "growing" part instead of plateau
                E1cap = min(E2, S2 + Lmin - 1)

                # Sum over the arithmetic part: E in [E0..E1cap]
                sum_arith = 0
                if E0 <= E1cap:
                    cnt1 = E1cap - E0 + 1
                    C = S1 + Lmin - 2
                    sum_arith = (E0 + E1cap - 2 * C) * cnt1 // 2

                # Plateau part: E in [plateau_start..E2], each with A starts
                plateau_start = max(E0, E1cap + 1)
                sum_plateau = 0
                if plateau_start <= E2:
                    sum_plateau = A * (E2 - plateau_start + 1)

                ans += sum_arith + sum_plateau

        return ans