class MedianFinder:

    def __init__(self):
        self.small_heap = []
        self.big_heap = []
        heapq.heapify(self.small_heap)
        heapq.heapify(self.big_heap)

    def addNum(self, num: int) -> None:
        if self.big_heap and num> self.big_heap[0]:
            heapq.heappush(self.big_heap,num)
        else:
            heapq.heappush(self.small_heap, -1 * num)
        if len(self.small_heap) > len(self.big_heap) +1:
            val = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.big_heap,val)
        if len(self.big_heap) > len(self.small_heap) +1:
            val = heapq.heappop(self.big_heap)
            heapq.heappush(self.small_heap,-1 *val)

    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.big_heap):
            return -1 * self.small_heap[0]
        elif len(self.big_heap) > len(self.small_heap):
            return self.big_heap[0]
        return (-1 * self.small_heap[0] + self.big_heap[0])/2.0
        
        