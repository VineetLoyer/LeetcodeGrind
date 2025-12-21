class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def get_soldier_count(row):
            low,high = 0,len(row)-1
            idx_of_last_one = -1
            while low<=high:
                mid = (low+high)//2
                if row[mid]==1:
                    idx_of_last_one = mid
                    low = mid+1
                else:
                    high = mid-1
            return idx_of_last_one+1
        
        heap = []
        for i,row in enumerate(mat):
            count = get_soldier_count(row)
            entry = (-count,-i)
            heapq.heappush(heap,entry)

            if len(heap)>k:
                heapq.heappop(heap)
        
        result = []
        while heap:
            val,idx = heapq.heappop(heap)
            result.append(-idx)
        
        return result[::-1]