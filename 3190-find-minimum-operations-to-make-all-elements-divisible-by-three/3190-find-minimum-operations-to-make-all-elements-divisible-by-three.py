class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            if (num-1)%3==0 or (num+1)%3==0:
                count+=1
        return count
            