class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # lets have a left and right product array
        n = len(nums)
        left=[1]*n
        right=[1]*n
        output=[0]*n
        for i in range(1,n):
            left[i]=left[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        
        for i in range(n):
            output[i]=left[i]*right[i]
        return output