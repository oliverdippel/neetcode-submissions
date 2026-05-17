class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = float("inf")
        profit = 0

        for i in prices:
            profit = max(profit, i - current_min)
            current_min = min(current_min, i)

        return profit