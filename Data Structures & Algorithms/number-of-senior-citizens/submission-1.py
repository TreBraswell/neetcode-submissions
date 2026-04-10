class Solution:
    def countSeniors(self, details: List[str]) -> int:
        r = 0
        for w in details:
            if int(w[11:13])>60:
                r+=1
        return r