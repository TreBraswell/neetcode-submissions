class TimeMap:

    def __init__(self):
        
        self.time_map = defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
         
        self.time_map[key].append([timestamp,value])
        print(self.time_map)

    def get(self, key: str, timestamp: int) -> str:
        # if len(timestamp[key])
        l = 0 
        r = len(self.time_map[key])-1
        sub_array = self.time_map[key]
        res = ""
        m = r
        while l <=r:
            m = (l+r)//2
            #print(m , " ", l, " ", r, ' ', sub_array[m][0], ' ', timestamp)
            if sub_array[m][0]>timestamp:
                r = m-1
            else:
                res = sub_array[m][1]
                l = m+1
                #return sub_array[m][1]

        return res
        
