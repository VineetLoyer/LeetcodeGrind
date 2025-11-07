from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        sum_occ = defaultdict(int)
        sum_occ[0]=1
        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in sum_occ:
                count+=sum_occ[prefix_sum - k]
            sum_occ[prefix_sum]+=1

        return count