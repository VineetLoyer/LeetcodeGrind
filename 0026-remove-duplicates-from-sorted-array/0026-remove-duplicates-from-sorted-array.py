class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        # i points to the last unique element
        i = 0
        for j in range(1, len(nums)):
            # If current is different from last unique, update next spot
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        # Return count of unique elements
        return i + 1
