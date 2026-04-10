class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # create an array of infinite prices 
        prices = [float("inf")] * n
        prices[src] = 0
        for ki in range(k+1):
            print(prices)
            temp_prices = prices.copy()
            for s,d,cost in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + cost < temp_prices[d]:
                    temp_prices[d] = prices[s] + cost
            prices = temp_prices
        
        if prices[dst] == float("inf"):
            return -1
        return prices[dst]