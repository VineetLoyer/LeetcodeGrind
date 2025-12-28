class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(firstList)
        m = len(secondList)
        if n==0 or m==0:
            return []
        i,j=0,0
        while i<n and j<m:
            lo = max(firstList[i][0],secondList[j][0])
            hi = min(firstList[i][1],secondList[j][1])

            if lo<=hi:
                res.append([lo,hi])
            
            if firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                j+=1
        
        return res
        