class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 1:
            return 1
        l = 0
        t = defaultdict(int)
        t[fruits[l]] +=1
        res = 0
        for r in range(1,len(fruits)):
            print(t ,len(t),l,r)
            t[fruits[r]] +=1
            while l <r and len(t) > 2:
                t[fruits[l]] -=1
                if t[fruits[l]] ==0:
                    del t[fruits[l]]
                l+=1
            res = max(res,1+(r-l))
        return res