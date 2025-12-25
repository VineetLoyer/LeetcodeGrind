class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k: 
                curr_sum = nums[i] + nums[j] + nums[k]
                if abs(curr_sum - target) < min_diff:
                    min_diff = abs(curr_sum - target)
                    closest_sum = curr_sum
                if curr_sum > target:
                    k -= 1
                elif curr_sum < target:
                    j += 1
                elif curr_sum == target:
                    return curr_sum 
        return closest_sum