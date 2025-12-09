MOD = 10**9 + 7
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left = defaultdict(int)
        right = defaultdict(int)
        for x in nums:
            right[x] += 1

        ans = 0
        for j, x in enumerate(nums):
            right[x] -= 1                     # j is no longer on the right
            target = 2 * x
            ans = (ans + left[target] * right[target]) % MOD
            left[x] += 1
        return ans % MOD
            