class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Idea is that there would be at most 2 elements that are greater than or equal to n/3 in frequency. Why? divide the array in 3 parts, there would be only 2 elements (at most) each 33% of total that would fit the criteria of majority n/3 freq.

        if not nums: return []
        candidate1,candidate2,count1,count2 = None, None, 0,0
        for num in nums:
            if num == candidate1:
                count1+=1
            elif num == candidate2:
                count2+=1
            elif count1==0:
                candidate1=num
                count1=1
            elif count2==0:
                candidate2=num
                count2=1
            else:
                count1-=1
                count2-=1
        return [c for c in {candidate1,candidate2} if nums.count(c)>len(nums)//3]