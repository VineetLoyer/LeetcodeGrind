class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        max_sum = 0
        while left<right:
            current_sum = nums[left]+nums[right]
            left+=1
            right-=1
            if current_sum>max_sum:
                max_sum = current_sum
        return max_sum