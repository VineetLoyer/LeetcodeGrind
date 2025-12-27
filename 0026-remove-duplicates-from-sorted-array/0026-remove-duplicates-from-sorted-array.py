class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # need one pointer that keeps track of unique elements, this fills array 
        # need another pointer to traverse the array in search of new elements.
        if not nums:
            return 0
        slow = 0
        for fast in range(1,len(nums)):
            if nums[fast]!=nums[slow]:
                slow+=1
                nums[slow]=nums[fast]
        return slow+1
        
