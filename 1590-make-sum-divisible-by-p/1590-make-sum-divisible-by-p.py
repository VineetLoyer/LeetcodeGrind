class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_rem = sum(nums)%p
        if total_rem == 0:
            return 0
        last = {0:-1}
        cur = 0
        res = len(nums)

        for i,x in enumerate(nums):
            cur = (cur+x)%p
            target = (cur-total_rem + p )%p
            if target in last:
                res = min(res,i-last[target])
            last[cur] = i
        return -1 if res==len(nums) else res