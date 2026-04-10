class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r= 0
        mx = 0
        while r != len(prices):
            gain = prices[r] - prices[l]
            mx = max(mx, prices[r] - prices[l])
            if prices[r] <prices[l]:
                l+=1
            else:
                r +=1
        return mx