class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # S = n*(n+1)//2
        # actual_sum = sum(nums)
        # unique_sum = sum(set(nums))
        # duplicate = actual_sum - unique_sum
        # missing = S - unique_sum
        # return [duplicate,missing]
        n = len(nums)
        #Exp sum
        # S = 1+2+3+....+n = n(n+1)/2
        # Q = 1^2 + 2^2 + 3^2 +.....+ n^2
        S = n*(n+1)//2 # expected sum
        Q = n*(n+1)*(2*n+1)//6 
        s = sum(nums) # actual sum
        q = sum(x*x for x in nums)

        delta = S - s  #m-d
        sigma = (Q-q)//delta #m+d

        m = (delta+sigma)//2
        d = m-delta
        return [d,m] 