class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.time_map:
            self.time_map[key]= [[value,timestamp]]
        else:
            self.time_map[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.time_map:
            return ""
        lst = self.time_map[key]
        res = ""
        l =0
        r = len(lst)-1
        while l<=r:
            m = (l+r)//2
            if lst[m][1] <= timestamp:
                res = lst[m][0]
                l = m + 1
            else:
                r = m-1
        return res
