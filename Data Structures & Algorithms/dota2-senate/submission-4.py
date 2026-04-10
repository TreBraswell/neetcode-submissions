class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        i = 0
        count = 0
        senate = list(senate)
        while i <len(senate)-1 and i !=100:
            print(senate,count, i,senate[i])
            if senate[i] == "R":
                if count<0:
                    count+=1
                    i+=1
                    continue
                senate.append("R")
                count+=1
            elif senate[i] == "D":
                if count>0:
                    count-=1
                    i+=1
                    continue
                senate.append("D")
                count-=1
            i+=1
        if senate[-1] == "R":
            return "Radiant"
        else:
            return "Dire"