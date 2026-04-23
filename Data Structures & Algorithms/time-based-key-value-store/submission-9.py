class TimeMap:

    def __init__(self):
        self.s = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.s[key].append((timestamp,value))
        return None

    def get(self, key: str, timestamp: int) -> str:
        v = self.s[key]
        l = 0
        r = len(v)-1
        res = ""
        while l <= r:
            m = (l +r)//2
            if v[m][0]> timestamp:
                r = m-1
            else:
                res = v[m][1]
                l = m+1
        return res
