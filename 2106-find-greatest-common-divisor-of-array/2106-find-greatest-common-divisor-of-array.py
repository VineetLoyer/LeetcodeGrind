def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # num1 = min(nums)
        # num2 = max(nums)
        nums.sort()
        a = nums[0]
        b = nums[-1]    
        return gcd(a,b)