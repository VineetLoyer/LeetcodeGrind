class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        i,j=0,0
        count = 0
        while i<len(arr1):
            countj = 0
            j=0
            while j<len(arr2):
                if abs(arr1[i]-arr2[j])<=d:
                    break
                else:
                    countj+=1
                    j+=1
            if countj==len(arr2):
                count+=1
            i+=1
        return count
                