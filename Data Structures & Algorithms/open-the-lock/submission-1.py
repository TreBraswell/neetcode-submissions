class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def make_locks(s):
            res = []
            for i in range(4):
                b = str((int(s[i]) + 1 )%10)
                res.append(s[:i] + b + s[i+1:])
                b = str((int(s[i]) - 1+10) %10)
                res.append(s[:i] + b + s[i+1:])
            return res
        visit = set(deadends)
        q = [(0,'0000')]
        while q:
            t,s = q.pop(0)
            if s in visit:
                continue
            if s == target:
                return t
            visit.add(s)
            for l in make_locks(s):
                if l in visit:
                    continue
                q.append((t+1,l))
        
        return -1