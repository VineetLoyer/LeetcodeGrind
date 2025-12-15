class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[index],nums[j] = nums[j],nums[index]
                index+=1
        
