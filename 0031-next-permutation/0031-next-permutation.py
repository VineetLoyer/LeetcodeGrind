class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i>=0:
            j = len(nums)-1
            while nums[j]<=nums[i]:
                j-=1
            nums[j],nums[i]=nums[i],nums[j]
        nums[i+1:]=reversed(nums[i+1:])
        

        # nums = [1,2,3]
        # i = len(nums)-2 = 1
        # i>=0 (yes) and nums[1] = 2 > nums[2]=3 No
        
        # i=1
        # j = 2
        # nums[j] (3)<nums[i](2) No
        # Swap [1,3,2]

        # nums[2+] = [1,3,2]

