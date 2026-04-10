class Twitter:

    def __init__(self):
        self.time = 0
        self.followmap  = defaultdict(set)
        self.tweetmap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append((tweetId,self.time))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        tweets = []
        self.followmap[userId].add(userId)
        for follower in self.followmap[userId]:
            if follower in self.tweetmap:
                index = len(self.tweetmap[follower])-1
                tweetid, time = self.tweetmap[follower][index]
                heapq.heappush(tweets,[time,tweetid,follower,index-1])
        res = []
        while tweets and len(res)<10:
            time,tweetid,follower,index = heapq.heappop(tweets)
            res.append(tweetid)
            if index>=0:
                tweetid, time = self.tweetmap[follower][index]
                heapq.heappush(tweets,[time,tweetid,follower,index-1])
        return res

        
                

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followmap and followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
