class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # lets have a left and right product array
        n = len(nums)
        ans = [1]*n
        pref = 1
        for i in range(n):
            ans[i] = pref
            pref*=nums[i]
        post = 1
        for i in range(n-1,-1,-1):
            ans[i]*=post
            post*=nums[i]
        return ans

         
 