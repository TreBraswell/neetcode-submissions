class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        c= columnNumber
        res=""
        while c>0:
            c -= 1
            offset = c%26
            nxt = chr(ord("A")+ offset)
            
            res = nxt + res
            c = c//26
        return res
