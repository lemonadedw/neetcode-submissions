class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_num = float('inf')

        for p in prices:
            if p < lowest_num:
                lowest_num = p
            
            max_profit = max(max_profit, p - lowest_num)

        return max_profit