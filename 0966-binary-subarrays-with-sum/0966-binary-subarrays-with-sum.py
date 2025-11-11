class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def at_most(S):
            if S<0:
                return 0
            ans = 0
            left = 0
            window_sum = 0
            for right,x in enumerate(nums):
                window_sum += x
                while window_sum>S:
                    window_sum-=nums[left]
                    left+=1
                ans+=right-left+1
            return ans
        return at_most(goal) - at_most(goal-1)