class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = []
        for i in stones:
            res.append(i*-1)
        heapq.heapify(res)
        while len(res)>1:
            one = heapq.heappop(res)*-1
            two = heapq.heappop(res)*-1
            val = abs(one - two) *-1
            if val != 0 or len(res) == 0:
                heapq.heappush(res,val)
        return heapq.heappop(res) *-1