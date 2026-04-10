class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f = 0
        t = 0
        for b in bills:
            change = b -5
            if change == 5:
                f -=1
            elif change == 10:
                if t >0:
                    t -= 1
                else:
                    f-=2
            elif change == 15:
                if f <3:
                    t-=1
                    f-=1
                else:
                    f-=3
            
            print(f,t)
            if f <0 or t <0:
                return False
            if b == 10:
                t+=1
            if b == 5:
                f+=1
        return True
                