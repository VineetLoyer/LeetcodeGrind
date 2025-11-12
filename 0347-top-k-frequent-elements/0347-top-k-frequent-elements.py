class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Top - k ? Buckets
        freq = Counter(nums)
        sorted_unique = sorted(freq, key=lambda x: -freq[x])
        return sorted_unique[:k]