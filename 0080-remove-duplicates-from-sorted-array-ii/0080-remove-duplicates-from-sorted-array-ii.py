class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2:
            return n
        index = 2
        for fast in range(2,n):
            if nums[fast]!=nums[index-2]:
                nums[index] = nums[fast]
                index+=1
        return index