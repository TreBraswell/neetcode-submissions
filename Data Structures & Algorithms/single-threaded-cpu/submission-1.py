class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        t = []
        for i,v in enumerate(tasks):
            t.append((v[0],v[1],i))
        tasks = t
        tasks.sort()
        print(tasks)
        h = []
        t,p,i = tasks.pop(0)
        heapq.heappush(h,(p,t,i))
        res = []
        while h:
            pp,tt,ii = heapq.heappop(h)
            t += pp
            res.append(ii)
            while tasks and tasks[0][0]<=t:
                tt,pp,ii = tasks.pop(0)
                heapq.heappush(h,(pp,tt,ii))
            if not h and tasks:
                tt,pp,ii = tasks.pop(0)
                t = tt
                heapq.heappush(h,(pp,tt,ii))
        return res

