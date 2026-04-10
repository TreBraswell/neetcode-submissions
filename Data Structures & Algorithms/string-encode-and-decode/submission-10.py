class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res =[]
        i = 0
        while len(s)>0 :
            h = s.find('#')
            sz = int(s[0:h])
            wrd = s[h+1:h+1+sz]
            res.append(wrd)
            s = s[h+1+sz:]
            print(s)
            i +=1
        return res




