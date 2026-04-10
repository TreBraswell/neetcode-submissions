class Solution:
    def decodeString(self, s: str) -> str:
        w = []
        res = ''
        for i in s:
            print(w)
            if i != ']':
                w.append(i)
            else:
                c = ''
                while w[-1] != '[':
                    c =  w.pop() + c
                    print(w,c)
                w.pop()
                k = ''
                while w and w[-1].isdigit():
                    k = w.pop() + k
                w.append(int(k)*c)
        while w:
            res = w.pop() + res
        return res
                