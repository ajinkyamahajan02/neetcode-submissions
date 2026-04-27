class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 0
        max_price = 0

        for i in range(len(prices)):

            if prices[i] > prices[max_price]:
                max_price = i
            
            if prices[i] < prices[min_price]:
                min_price = i
            
            if max_price > min_price:
                max_profit = max(max_profit, (prices[max_price]- prices[min_price]))

            if max_price < min_price:
                max_price = min_price 
                
        return max_profit        