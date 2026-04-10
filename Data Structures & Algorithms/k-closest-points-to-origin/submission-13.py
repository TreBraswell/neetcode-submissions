class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x,y in points:
            dist = (x**2) + y**2
            min_heap.append([dist,[x,y]])
        heapq.heapify(min_heap)
        res =[]
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res