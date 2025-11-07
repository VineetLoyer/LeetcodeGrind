class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expSum = (((n+1)*(n))//2)
        print(expSum)
        recSum=0
        for num in nums:
            recSum+=num
        return expSum-recSum
