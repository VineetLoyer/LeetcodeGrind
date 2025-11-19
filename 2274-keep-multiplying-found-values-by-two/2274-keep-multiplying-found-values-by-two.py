class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)
        result = original
        while result in num_set:
            result*=2
        return result