class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones:
            return n-ones
        best_len = float('inf')
        for i in range(n):
            g = nums[i]
            if g==1:
                best_len = 1
                break
            for j in range(i+1,n):
                g = gcd(g,nums[j])
                if g==1:
                    best_len = min(best_len,j-i+1)
                    break
        if best_len == float('inf'):
            return -1
        
        return n+best_len-2