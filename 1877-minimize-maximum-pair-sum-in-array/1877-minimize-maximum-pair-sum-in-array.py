class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # 2,3,4,4,5,6 => (2,6),(3,5),(4,4)
        # 2,3,3,5 => (2,5),(3,3)
        nums.sort()
        left=0
        right=len(nums)-1
        maxp = 0
        while left<right:
            cur_sum = nums[left]+nums[right]
            if cur_sum>=maxp:
                maxp=cur_sum
            left+=1
            right-=1
        return maxp