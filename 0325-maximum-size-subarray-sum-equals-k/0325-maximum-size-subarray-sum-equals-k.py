class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        seen = {0:-1}
        maxLen = 0
        for i, n in enumerate(nums):
            prefixSum+=n
            if prefixSum-k in seen:
                maxLen = max(maxLen,i-seen[prefixSum-k])
            if prefixSum not in seen:
                seen[prefixSum]=i
        return maxLen