class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fa = [] #array to store factors
        for i in range(1,n+1):
            if n%i==0:
                fa.append(i)
        print(fa)
        if k<=len(fa):
            return fa[k-1]
        else:
            return -1