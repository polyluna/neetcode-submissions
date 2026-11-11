class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxp = 0
        
        for sell in prices:
            maxp = max(maxp, sell-minBuy)
            minBuy = min(minBuy,sell)
        return maxp