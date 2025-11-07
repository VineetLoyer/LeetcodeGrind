class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for current in range(len(nums)):
            if nums[current]!=0:
                nums[left],nums[current]=nums[current],nums[left]
                left+=1