class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # idea is I keep both the max and min product ending at the current index ( a negative can flip a small negative into big positive).
        cur_max = cur_min = ans = nums[0]
        for x in nums[1:]:
            if x<0:
                cur_max,cur_min = cur_min,cur_max
            cur_max = max(x,cur_max*x)
            cur_min = min(x,cur_min*x)
            ans = max(ans,cur_max)
        return ans