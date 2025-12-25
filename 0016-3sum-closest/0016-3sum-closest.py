class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left,right = i+1,len(nums)-1
            while left<right:
                cur_sum = nums[i]+nums[left]+nums[right]
                if abs(target-cur_sum)<abs(target-closest_sum):
                    closest_sum = cur_sum
                if cur_sum==target:
                    return target
                if cur_sum<target:
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    
                else:
                    right-=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
        return closest_sum

