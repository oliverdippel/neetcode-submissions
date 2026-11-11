class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_min = float("inf")
        
        for i in prices:
            if i < current_min:
                current_min = i
            else:
                max_profit = max(max_profit, i - current_min)

        return max_profit