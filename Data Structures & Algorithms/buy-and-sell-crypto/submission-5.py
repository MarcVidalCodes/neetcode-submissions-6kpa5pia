class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        buy = 0

        for i in range(1, len(prices)): 
            sell = i
            profit = prices[sell] - prices[buy] 

            if prices[sell] < prices[buy]: 
                buy = sell
            
            max_profit = max(max_profit, profit)

        return max_profit