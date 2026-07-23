class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 1
        profit = 0

        while s < len(prices):
            if prices[b] < prices[s]:
                profit = max(prices[s] - prices[b], profit)
            else:
                b = s
            s += 1
        return profit
