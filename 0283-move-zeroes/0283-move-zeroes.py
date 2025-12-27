class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=0
        for fast in range(len(nums)):
            if nums[fast]!=0:
                nums[index],nums[fast]=nums[fast],nums[index]
                index+=1