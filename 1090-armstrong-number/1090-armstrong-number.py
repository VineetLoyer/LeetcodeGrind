class Solution:
    def isArmstrong(self, n: int) -> bool:
        # count the number of digits in n
        count = 0
        original1,org2 = n,n
        n = abs(n)
        while n > 0:
            n //= 10
            count += 1
        
        #a k-digit armstrong
        sumd=0
        while original1>0:
            ld = original1%10
            kld = ld**count
            sumd+=kld
            original1//=10
        return sumd==org2