class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        #Pass1: count zeroes
        zeros = 0
        for num in arr:
            if num==0:
                zeros+=1
        n = len(arr)
        for i in range(n-1,-1,-1):
            if i+zeros < n:
                arr[i+zeros] = arr[i]
            if arr[i]==0:
                zeros-=1
                if i+zeros<n:
                    arr[i+zeros]=0


        