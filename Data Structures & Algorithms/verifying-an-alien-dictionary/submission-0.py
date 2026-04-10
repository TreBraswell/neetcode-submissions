class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = {}
        for i,v in enumerate(order):
            pos[v] = i
        print(pos)
        for i in range(len(words)):
            if i + 1 == len(words):
                break
            f= words[i]
            s = words[i+1]
            l= min(len(f),len(s))
            for ii in range(l):
                if pos[f[ii]]<pos[s[ii]]:
                    break

                if pos[f[ii]]>pos[s[ii]]:
                    return False
                print(ii,f,s)
            if f[:l]== s[:l] and len(f)> len(s):
                return False
        return True
            
