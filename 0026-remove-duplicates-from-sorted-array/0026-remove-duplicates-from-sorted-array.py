class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0 # ptr1
        for j in range(1,len(nums)): #ptr2
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1