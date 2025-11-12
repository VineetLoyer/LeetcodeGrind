class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        ans = 0
        s = 0
        for x in nums:
            s+=x
            r=s%k
            ans+=freq[r]
            freq[r]+=1
        return ans