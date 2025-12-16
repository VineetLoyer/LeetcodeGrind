class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even_ptr = 0
        odd_ptr = 1
        while even_ptr<n and odd_ptr<n:
            while even_ptr<n and nums[even_ptr]%2==0:
                even_ptr+=2
            while odd_ptr<n and nums[odd_ptr]%2!=0:
                odd_ptr+=2
            if even_ptr<n and odd_ptr<n:
                nums[even_ptr],nums[odd_ptr] = nums[odd_ptr],nums[even_ptr]
                even_ptr+=2
                odd_ptr+=2
        return nums