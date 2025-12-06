MOD = 10**9+7
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        pref = [0] * (n + 2)

        dp[0] = 1
        pref[1] = 1  # pref[1] = dp[0]

        maxdq = deque()
        mindq = deque()
        L = 0

        for r, x in enumerate(nums):
            # insert into max deque
            while maxdq and nums[maxdq[-1]] <= x:
                maxdq.pop()
            maxdq.append(r)

            # insert into min deque
            while mindq and nums[mindq[-1]] >= x:
                mindq.pop()
            mindq.append(r)

            # shrink from left until window is valid
            while nums[maxdq[0]] - nums[mindq[0]] > k:
                if maxdq[0] == L:
                    maxdq.popleft()
                if mindq[0] == L:
                    mindq.popleft()
                L += 1

            # all starts j in [L, r] are valid
            dp[r + 1] = (pref[r + 1] - pref[L]) % MOD

            # update prefix sum
            pref[r + 2] = (pref[r + 1] + dp[r + 1]) % MOD

        return dp[n]