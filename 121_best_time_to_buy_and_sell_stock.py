class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # prices[i] is the price given on the ith day
        # maximize profit by buying one a single day and then selling on the next day
        # 

        left = 0
        right = 1
        profit = 0

        while right < len(prices):
            
            # Since the profit will be negative in this case
            if prices[right] > prices[left]:
                profit = max(profit, prices[right] - prices[left])
            else:
                left = right
            right += 1
        
        return profit


            
        