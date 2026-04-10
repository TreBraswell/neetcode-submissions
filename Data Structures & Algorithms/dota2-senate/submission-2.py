class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        last_skip = ""
        r_s =0
        d_s = 0
        r_count = 0
        d_count = 0
        for i in senate:
            if i == "R":
                if d_s>0:
                    last_skip = "Radiant"
                    d_s-=1
                    continue
                else:
                    r_s +=1
                    r_count+=1
            else:
                if r_s>0:
                    r_s-=1
                    last_skip = "Dire"
                    continue
                else:
                    d_s +=1
                    d_count +=1
        while r_s!= 0:
            d_count-=1
            r_s-=1
            last_skip = "Dire"
        while d_s!= 0:
            r_count-=1
            d_s-=1 
            last_skip = "Radiant"       
        if r_count>d_count:
            return "Radiant"
        elif d_count>r_count:
            return "Dire"
        else:
            return last_skip

        