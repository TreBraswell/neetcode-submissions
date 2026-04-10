class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        res = [-i for i in count.values()]
        time = 0 
        heapq.heapify(res)
        queue = []
        while queue or res:
            time +=1
            if res:
                val = heapq.heappop(res)
                val +=1
                if val !=0:
                    queue.append([val,time+n])
            if queue and queue[0][1] == time:
                heapq.heappush(res,queue.pop(0)[0])
        return time