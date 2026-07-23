class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i, price in enumerate(prices):
            for j in range(i + 1, len(prices)):
                diff = prices[j] - price
                res = diff if diff > res else res
        return res