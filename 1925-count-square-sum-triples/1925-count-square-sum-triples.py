class Solution:
    def countTriples(self, n: int) -> int:
        sq = {i*i for i in range(1,n+1)}
        ans= 0
        for a in range(1,n+1):
            a2 = a*a
            for b in range(1,n+1):
                s = a2 + b*b
                if s in sq:
                    ans+=1
        return ans