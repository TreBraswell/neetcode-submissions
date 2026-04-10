class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetmap = defaultdict(list)
        self.followmap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append((self.time,tweetId))
        self.time-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.followmap[userId].add(userId)
        for followeeid in self.followmap[userId]:
            if followeeid in self.tweetmap:
                index = len(self.tweetmap[followeeid]) -1
                count, tweetid = self.tweetmap[followeeid][index]
                heapq.heappush(minheap,[count,tweetid,followeeid,index-1])
        while minheap and len(res)<10:
            count,tweetid,followeeid,index = heapq.heappop(minheap)
            res.append(tweetid)
            if index>=0:
                count,tweetid = self.tweetmap[followeeid][index]
                heapq.heappush(minheap,[count,tweetid,followeeid,index-1])
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followmap and followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
