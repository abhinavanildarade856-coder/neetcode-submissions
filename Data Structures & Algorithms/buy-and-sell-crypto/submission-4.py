class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l =0 
        r =1
        maxp =0 
        

        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxp = max(maxp,profit)
                
            else:
                l = r
            
            
        return maxp








        