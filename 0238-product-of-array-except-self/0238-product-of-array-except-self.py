class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # lets have a left and right product array
        n = len(nums)
        # ans = [1]*n
        # pref = 1
        # for i in range(n):
        #     ans[i] = pref
        #     pref*=nums[i]
        # post = 1
        # for i in range(n-1,-1,-1):
        #     ans[i]*=post
        #     post*=nums[i]
        # return ans
        posArr = [1]*n
        preArr = [1]*n
        for i in range(1,n):
            # [1,2,3,4] -> preArr = [0,1,2,6] 
            preArr[i] = preArr[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            # [1,2,3,4] -> posArr = [24,12,4,0]
            posArr[i]=posArr[i+1] * nums[i+1]
        result = [preArr[i]*posArr[i] for i in range(n)]
        return result
