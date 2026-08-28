class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                potentialProfit = prices[j]-prices[i]
                if potentialProfit > maxProfit:
                    maxProfit = potentialProfit
        
        return maxProfit
        