class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Top - k ? Buckets
        freq = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        for nums,c in freq.items():
            buckets[c].append(nums)
        ans = []
        for f in range(n,0,-1):
            for num in buckets[f]:
                ans.append(num)
                if len(ans)==k:
                    return ans