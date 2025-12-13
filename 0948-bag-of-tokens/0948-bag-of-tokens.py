class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left = 0
        right = len(tokens)-1
        score = 0
        max_score = 0
        while left <= right:
            #Option1: play face-up; if have enough power, buy the cheapest point(left)
            if power>=tokens[left]:
                power-=tokens[left]
                score+=1
                left+=1
                max_score = max(score,max_score)
            #option2: Play face-down; if we need power and have score to spend, sell a point for max_power(right)
            elif score>0:
                power+=tokens[right]
                score-=1
                right-=1
            #option3: stuck, can't buy score, can't buy power, game over.
            else:
                break
        return max_score
