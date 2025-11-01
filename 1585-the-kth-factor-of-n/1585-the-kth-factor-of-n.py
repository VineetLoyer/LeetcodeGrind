class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # fa = [] #array to store factors
        # for i in range(1,n+1):
        #     if n%i==0:
        #         fa.append(i)
        # print(fa)
        # if k<=len(fa):
        #     return fa[k-1]
        # else:
        #     return -1
        count = 0
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                count+=1
                if count==k:
                    return i
        factors = []
        for i in range(int(n**0.5),0,-1):
            if n%i==0 and i!=n//i:
                factors.append(n//i)
        for factor in factors:
            count+=1
            if count==k:
                return factor
        return -1