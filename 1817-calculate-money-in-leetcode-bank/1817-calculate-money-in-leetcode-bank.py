class Solution:
    def totalMoney(self, n: int) -> int:
        WC = n//7
        RC = n%7
        sd = 1
        ed = 7
        Sum = 0
        for i in range(WC):
            Sum += (7*(sd+ed))//2
            sd+=1
            ed+=1
        if RC>0:
            Sum += (RC * (2*sd + (RC-1)))//2
        return Sum
