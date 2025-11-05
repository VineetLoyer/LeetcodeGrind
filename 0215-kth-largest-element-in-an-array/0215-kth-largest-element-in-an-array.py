class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min_heap = []
        # for num in nums:
        #     heapq.heappush(min_heap,num)
        #     if len(min_heap)>k:
        #         heapq.heappop(min_heap)
        # return min_heap[0]
        min_value = min(nums)
        max_value = max(nums)
        count = [0]*(max_value - min_value +1)
        for num in nums:
            count[num-min_value]+=1
        remain=k
        for num in range(len(count)-1,-1,-1):
            remain -= count[num]
            if remain<=0:
                return num+min_value
        return -1