class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        missingEle = 0
        for num in nums:
            missingEle^=num
        return missingEle