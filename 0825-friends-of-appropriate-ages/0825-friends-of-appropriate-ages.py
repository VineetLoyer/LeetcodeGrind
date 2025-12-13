class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        n = len(ages)
        total_req = 0
        left = 0
        right = 0 
        for i in range(n):
            lower_bound = 0.5*ages[i]+7
            while left<n and ages[left]<=lower_bound:
                left+=1
            while right+1 <n and ages[right+1]<=ages[i]:
                right+=1
            if right>=left:
                total_req +=(right-left)
        return total_req