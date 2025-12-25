class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        left = 0
        right = len(nums)-1
        res = 0
        while left<=right:
            if nums[left]+nums[right]>target:
                right-=1
            else:
                res+=pow(2,right-left,MOD)
                res%=MOD
                left+=1
        return res