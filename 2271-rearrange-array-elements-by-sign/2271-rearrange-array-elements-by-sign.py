class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tmp = [0] * n
        pos = 0
        neg = n // 2

        for x in nums:
            if x > 0:
                tmp[pos] = x
                pos += 1
            else:
                tmp[neg] = x
                neg += 1

        result = []
        for i in range(n // 2):
            result.append(tmp[i])         # positive
            result.append(tmp[i + n//2])  # negative
        return result