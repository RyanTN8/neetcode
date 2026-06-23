class Twitter:

    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # add tweetID to hashMap[userID] (list(tuples)) - initialize if neccesary

        if userId in self.tweets:
            self.tweets[userId].append((self.count, tweetId))
            self.count += 1
        else:
            self.tweets[userId] = [(self.count, tweetId)]
            self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # check if userId follows themself, if not make them
        # iterate through follows, add each list to result
        # max heap the list and pop the top 10 elements

        if userId not in self.follows:
            self.follows[userId] = []
        if userId not in self.follows[userId]:
            self.follows[userId].append(userId)

        heap = []
        result = []
        for followee in self.follows[userId]:
            if followee in self.tweets:
                heap.extend(self.tweets[followee][-10:])
        heapq.heapify_max(heap)
        for i in range(min(10, len(heap))):
            result.append(heapq.heappop_max(heap)[1])

        return result
    def follow(self, followerId: int, followeeId: int) -> None:
        # add folloeeId to hashMap[followerId] (list) - initialize if necessary

        if followerId == followeeId or (followerId in self.follows and followeeId in self.follows[followerId]):
            return None
        if followerId not in self.follows:
            self.follows[followerId] = []
        self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove followeeId from hashMap[followerId] (list)

        if followerId == followeeId or followerId not in self.follows or followeeId not in self.follows[followerId]:
            return None
        self.follows[followerId].remove(followeeId)
