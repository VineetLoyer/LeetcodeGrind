class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        
        total = 0
        dec = 0 

        for i in range(k):
            if i >= len(happiness):
                break
            cur = happiness[i] - dec
            if cur <= 0:
                break
            total += cur
            dec += 1

        return total