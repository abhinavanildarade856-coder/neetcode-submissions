class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0 
        ot = 0

        for r in range( 1,len(prices)):
            if prices[r] > prices[r-1]:
                ot += prices[r] - prices[r-1]


        return ot

