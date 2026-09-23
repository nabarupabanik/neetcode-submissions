class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        l=0
        r=1
        max_p=0
        while r<len(prices):
            if prices[l] >= prices[r]:
                l=r
                
            else:
                profit=prices[r]-prices[l]
                max_p=max(max_p, profit)
            r+=1
        return max_p
