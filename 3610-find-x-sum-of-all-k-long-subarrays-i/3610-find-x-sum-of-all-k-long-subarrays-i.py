from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        if k > n: 
            return []
        
        MAXV = 50  # per constraints
        freq = [0] * (MAXV + 1)

        # build first window
        for j in range(k):
            freq[nums[j]] += 1

        def window_x_sum() -> int:
            # values 1..50 sorted by (-count, -value)
            order = sorted(range(1, MAXV + 1), key=lambda v: (-freq[v], -v))
            take = 0
            s = 0
            for v in order:
                if freq[v] == 0:
                    break
                s += v * freq[v]
                take += 1
                if take == x:
                    break
            return s

        ans = [window_x_sum()]

        # slide the window
        for i in range(k, n):
            out_v = nums[i - k]
            in_v  = nums[i]
            freq[out_v] -= 1
            freq[in_v]  += 1
            ans.append(window_x_sum())

        return ans
