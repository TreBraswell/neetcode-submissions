class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = []
        for i in stones:
            min_heap.append(i*-1)
        heapq.heapify(min_heap)
        while len(min_heap)>1:
            one = heapq.heappop(min_heap) * -1
            two = heapq.heappop(min_heap) * -1
            res = one - two
            if res != 0:
                heapq.heappush(min_heap,res*-1)
        if not min_heap:
            return 0
        return min_heap[0]*-1