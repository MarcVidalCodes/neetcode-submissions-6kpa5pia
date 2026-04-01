class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: 
            return 0

        max_profit = 0 
        buy = 0

        for i in range(1,len(prices)):
            profit = prices[i] - prices[buy]

            if prices[i] < prices[buy]:
                buy = i 
            
            max_profit = max(profit, max_profit)

        return max_profit
            

            