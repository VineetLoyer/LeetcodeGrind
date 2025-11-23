class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        rem1, rem2 = [], []
        for x in nums:
            if x % 3 == 1:
                rem1.append(x)
            elif x % 3 == 2:
                rem2.append(x)
        rem1.sort()
        rem2.sort()
        ans = 0
        r = total % 3
        if r == 0:
            return total
        elif r == 1:
            choices = []
            if rem1: choices.append(total - rem1[0])
            if len(rem2) >= 2: choices.append(total - rem2[0] - rem2[1])
            ans = max(choices) if choices else 0
        else:  # r == 2
            choices = []
            if rem2: choices.append(total - rem2[0])
            if len(rem1) >= 2: choices.append(total - rem1[0] - rem1[1])
            ans = max(choices) if choices else 0
        return ans
           