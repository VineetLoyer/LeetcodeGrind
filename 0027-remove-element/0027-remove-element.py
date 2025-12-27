class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        index = 0
        for fast in range(len(nums)):
            if nums[fast]!=val:
                nums[index]=nums[fast]
                index+=1
        return index
                
        