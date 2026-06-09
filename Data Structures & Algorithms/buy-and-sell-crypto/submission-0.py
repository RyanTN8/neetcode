class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = prices[0]
        maxProfit = 0
        for price in prices:
            maxProfit = max(maxProfit, price - currMin)
            currMin = min(currMin, price)
        return maxProfit
