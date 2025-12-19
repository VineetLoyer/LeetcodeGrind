class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        
        j = 0
        count = 0

        m = len(arr2)

        for val in arr1:
            while j<m and arr2[j]<val-d:
                j+=1

            if j==m or arr2[j]>(val+d): 
                count+=1

        return count
            