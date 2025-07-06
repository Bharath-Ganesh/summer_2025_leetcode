"""

every user
1. User can post
2. Follow/ Unfollow
3. Top 10 tweets

"""
import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.TWEET_COUNT = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.TWEET_COUNT -= 1
        self.tweets[userId].append((self.TWEET_COUNT, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        all_followers = self.followers[userId] | {userId}
        top_10_feeds = []
        most_recent_tweets = []
        for follower in all_followers:
            # recent tweets
            recent_tweets = self.tweets[follower][::-1]
            length = min(10, len(recent_tweets))
            for idx in range(length):
                self.TWEET_COUNT, tweetId = recent_tweets[idx]
                heapq.heappush(most_recent_tweets, (self.TWEET_COUNT, tweetId))

        for i in range(10):
            if not most_recent_tweets:
                break
            top_10_feeds.append(heapq.heappop(most_recent_tweets)[1])
        return top_10_feeds

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        #  User with user Id : 1 want to follow user id: 2
        # Follower ID : 1; Followee ID = id: 2
        self.followers[followeeId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.followers:
            self.followers[followeeId].remove(followerId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

if __name__ == '__main__':
    twitter = Twitter()

    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))  # ➤ [5]

    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))  # ➤ [6, 5]

    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))  # ➤ [5]