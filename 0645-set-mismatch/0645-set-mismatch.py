class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        S = n*(n+1)//2
        actual_sum = sum(nums)
        unique_sum = sum(set(nums))
        duplicate = actual_sum - unique_sum
        missing = S - unique_sum
        return [duplicate,missing]