class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0 # counts possible triplets
        n = len(nums)
        for i in range(n-1,1,-1): #we start with fixing largest side
            side3 = nums[i]
            left = 0
            right = i-1
            while left<right:
                if nums[left]+nums[right]>side3: #sum of two sides > third  
                    count+=(right-left)
                    right-=1
                else:
                    left+=1
        return count
                