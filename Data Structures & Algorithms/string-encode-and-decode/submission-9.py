class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) ==0:
            return 'none'
        res = ''
        for word in strs:
            for i in word:
                res= res + str(ord(i)) +'&'
            res = res[0:len(res)-1] + 'V'
        res = res[0:len(res)-1] 
        return res
            


    def decode(self, s: str) -> List[str]:
        if s == 'none':
            return []
        res = []
        for word in s.split('V'):
            res2 = ''
            for i in word.split('&'):
                if len(i) == 0:
                    continue
                res2 = res2 + chr(int(i))
            res.append(res2)
        return res

