class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        comb = [(position[i], speed[i])for i in range(len(position))]
        s =[]
        for i,v in sorted(comb)[::-1]:
            t= (target -i)/v
            s.append(t)
            if len(s) >1 and s[-1] <= s[-2]:
                s.pop()
        return len(s)