class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l= 0
        r = len(people)-1
        res = 0
        while l<=r:
            #print(l,r,res,limit,people)
            if r-1  >=l and people[r] +people[r-1] <=limit:
                #print('r first')
                res +=1
                r -=1
                r -=1
            elif people[r] + people[l] <= limit:
                #print('combined')
                res +=1
                l+=1
                r-=1
            elif r-1  >=l and people[r] <= limit:
                #print('equal')
                r-=1
                res+=1
            elif l+1 <=r and people[l] +people[l+1] <=limit:
                #print('double l')
                res +=1
                l +=1
                l +=1
            else:
                
                #print('this l')
                l+=1
                res +=1
                
        return res


