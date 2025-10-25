class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Brute force: check for all possible combinations
        # res = 0 
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i+1,len(prices)):
        #         sell = prices[j]
        #         res = max(res,sell-buy)
        # return res
        # Optimal Solution? 

        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price<min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit