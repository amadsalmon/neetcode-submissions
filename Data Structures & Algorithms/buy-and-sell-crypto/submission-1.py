class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuyPrice = 101  # 0 <= prices[i] <= 100
        
        for i in range(0, len(prices)):
            
            potentialProfit = prices[i] - minBuyPrice
            if potentialProfit > maxProfit:
                maxProfit = potentialProfit

            if prices[i] < minBuyPrice: 
                minBuyPrice = prices[i]


        return maxProfit
        