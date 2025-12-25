class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left<right:
            current_total = numbers[left]+numbers[right]
            if current_total<target:
                left+=1
            elif current_total>target:
                right-=1
            else:
                return [left+1,right+1]