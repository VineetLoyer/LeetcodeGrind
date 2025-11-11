class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k==0:
            return []
        dq = deque() #stores the indices, values decresing 
        res = []
        for i,x in enumerate(nums):
            while dq and nums[dq[-1]]<=x:
                dq.pop()
            dq.append(i)
            if dq[0]<=i-k:
                dq.popleft()
            if i>=k-1:
                res.append(nums[dq[0]])
        return res