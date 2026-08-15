class Solution(object):
    def maxProfit(self, prices):
        lowest = prices[0]
        result = 0
        for i in range(len(prices)):
            if prices[i] < lowest:
               lowest = prices[i]
            if prices[i] - lowest > result:
               result = prices[i] - lowest
        return result


        
        