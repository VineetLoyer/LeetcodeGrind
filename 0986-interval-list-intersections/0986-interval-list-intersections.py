class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i =0 
        j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            
            # Let's start by finding the overlap range
            # firstList[i][0] is the start of interval A
            # firstList[i][1] is the end of interval A
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            
            # If valid intersection, add it
            if lo <= hi:
                res.append([lo, hi])
            
            # THE POINTER LOGIC:
            # If interval A ends before interval B, we are done with A.
            # Move to the next interval in A.
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
                
        return res

        
