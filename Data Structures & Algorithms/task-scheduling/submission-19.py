class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = 0 
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        queue = []
        while len(queue)>0 or len(maxHeap)>0:
            t +=1
            #check heap
            if maxHeap:
                ele = heapq.heappop(maxHeap)+1           
                if ele != 0:
                    queue.append([t +n,ele])
            if queue and  queue[0][0] == t:
                temp = queue.pop(0)
                heapq.heappush(maxHeap,temp[1])
        return t
