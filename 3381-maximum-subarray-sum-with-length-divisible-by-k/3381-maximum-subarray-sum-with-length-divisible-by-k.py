class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0]
        for x in nums:
            prefix_sum.append(prefix_sum[-1] + x)
        result = float('-inf')
        min_prefix = {}
        for i in range(n+1):
            mod_key = i%k
            if mod_key in min_prefix:
                result = max(result,prefix_sum[i] - min_prefix[mod_key])
            if mod_key not in min_prefix:
                min_prefix[mod_key] = prefix_sum[i]
            min_prefix[mod_key] = min(min_prefix[mod_key], prefix_sum[i])
        return result