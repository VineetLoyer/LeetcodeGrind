class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 2
        for j in range(2,len(nums)):
            if nums[j]!=nums[index-2]:
                nums[index]=nums[j]
                index+=1
        return index