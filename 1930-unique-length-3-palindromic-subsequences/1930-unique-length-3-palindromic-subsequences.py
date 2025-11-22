class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)

        # first[i], last[i] store first and last positions of chr(i + 'a')
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = max(last[idx], i)

        ans = 0

        # For each character as the outer char of the palindrome: c ? c
        for c in range(26):
            l, r = first[c], last[c]
            if l < r:  # need at least 2 occurrences of this char
                # collect distinct middle characters between l and r
                middle_chars = set(s[l + 1:r])
                ans += len(middle_chars)

        return ans