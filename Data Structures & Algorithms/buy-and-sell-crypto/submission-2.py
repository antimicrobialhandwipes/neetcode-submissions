class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_profit = 0

        for buy_price_index in range(0, len(prices) - 1):
            for sell_price_index in range(buy_price_index, len(prices)):
                current_profit = prices[sell_price_index] - prices[buy_price_index]
                if current_profit > max_profit:
                    max_profit = current_profit
        
        return max_profit