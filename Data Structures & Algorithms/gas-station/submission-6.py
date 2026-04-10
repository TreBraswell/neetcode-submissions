class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)< sum(cost):
            return True *-1
        dist = []
        for i in range(len(gas)):
            dist.append(gas[i] - cost[i])
        cur_i =-1
        cur_sum = 0
        res =0
        print(dist)    
        for i in range(len(dist)):
            print(cur_i,cur_sum)
            if cur_i != -1:
                cur_sum += dist[i]
            if cur_sum <0:
                cur_i = -1
                cur_sum = 0
            if cur_i == -1  and dist[i] >= 0 :
                cur_i = i
                cur_sum = dist[i]
        if cur_i == -1:
            return True *-1
        return cur_i
