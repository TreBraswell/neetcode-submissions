class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        g = sum(piles)/2
        def backtrack(p,s,alices_turn):
            # print(s,p)
            if not p:
                return s>g
            if alices_turn:
                l = p.pop()
                r = backtrack(p,s + l,False)
                if r:
                    return r
                p.append(l)
                
                l = p.pop(0)
                rr = backtrack(p,s + l,False)
                p.insert(0,l)
                return rr or r
            else:
                l = p.pop()
                r = backtrack(p,s,True)
                if r:
                    return r
                p.append(l)
                
                l = p.pop(0)
                rr = backtrack(p,s,True)
                p.insert(0,l)
                return rr or r   

        return backtrack(piles,0,True)