class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p,n=0,1 #pointers of pos and neg elements
        results=[0]*len(nums)
        for i in nums:
            if i>=0:
                results[p]=i
                p+=2
            else:
                results[n]=i
                n+=2
        return results
