# 這題是要做出一個簡單的推特，有以下幾個功能
# 初始化的部分需要幾個東西
  # follows 存說誰追蹤了誰，方便後面去找要給哪位使用者看哪些推
  # user_tweet 存該使用者他自己發的推
  # post 來記錄發文先後順序
# postTweet 是用來說某個使用者發了某篇推文，然後會給發推 ID(tweetId)
  # 這邊就是先把 post 加一，然後再把推文 ID 加進去發文者的紀錄檔裡面
  # 同時再檢查一下看有沒有超過 10 篇推文，有的話就刪掉最舊的那一篇
# getNewsFeed 是用來回傳某個使用者最近可以看到的 10 篇推文(含自己發推跟追隨者發推)
  # 做法就是先把使用的發的推拿出來做成 heap (因為前面有控制數量不大於10，所以這邊在操作的時候會比較快一點，可以少跑一些老舊推文)
  # 然後就從該使用者的跟隨列表中，把每個跟隨者的文章逐一拿出來做推文的比對，把比較新的留著，舊的丟出 heap (這裡用 heappushpop 比較快)
  # 最後就可以從heap裡面倒序回傳成 list 就可以了
# follow 是用來記錄說使用者跟隨了誰，直接在 self.follows 裡面做新增就好了
# nufollow 就是跟 follow 一樣直接做就可以了，把取消跟隨的 ID 那項給移除就行了
# 這題真的好難喔幹，難怪我就是個 code 廢物

class Twitter:

    def __init__(self):
        self.follows = collections.defaultdict(set)
        self.user_tweet = collections.defaultdict(collections.deque)
        self.post = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post += 1
        tweets = self.user_tweet[userId]
        tweets.append(((self.post),tweetId))
        if len(tweets)>10:
            tweets.popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        h = list()
        h.extend(self.user_tweet[userId])
        heapify(h)
        for user in self.follows[userId]:
            tweets = self.user_tweet[user]
            for x in range(len(tweets)-1, -1, -1):
                if len(h) < 10:
                    heappush(h, tweets[x])
                else:
                    if h[0][0] < tweets[x][0]:
                        heappushpop(h, tweets[x])
                    else:
                        break
        return [heappop(h)[1] for x in range(len(h))][::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
