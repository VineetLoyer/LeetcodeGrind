class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0
        i = 1
        Sum = 0
        while 5**i<=n:
            Sum += (n//5**i)
            i+=1
        return Sum