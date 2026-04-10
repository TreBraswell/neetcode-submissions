class Twitter:

    def __init__(self):
        self.tweetmap = defaultdict(list)
        self.followmap = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append((self.time,tweetId))
        self.time -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        self.followmap[userId].add(userId)
        for follow_id in self.followmap[userId]:
            if follow_id in self.tweetmap:
                index = len(self.tweetmap[follow_id])-1
                time,tweetId = self.tweetmap[follow_id][index]
                heapq.heappush(min_heap,[time,tweetId,follow_id,index-1])
        while min_heap and len(res) <10:
            time,tweetId,follow_id,index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index>=0:
                time,tweetId = self.tweetmap[follow_id][index]
                heapq.heappush(min_heap,[time,tweetId,follow_id,index-1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followmap and followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
