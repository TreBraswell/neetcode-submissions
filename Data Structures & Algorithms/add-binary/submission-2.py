class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = max(len(a), len(b))
        res=""
        carry = 0
        for i in range(l):
            a_b = 0

            if i<len(a) and a[len(a)-1-i]== "1":
                a_b=1
            b_b = 0
            if i <len(b) and b[len(b)-1-i]=="1":
                b_b = 1
            t = b_b + a_b + carry
            if t >1:
                carry = 1
            else:
                carry =0
            t= t%2
            if t == 1:
                res = "1"+ res
            else:
                res = "0"+ res
        if carry:
            res ="1"+ res 
        return res




                


