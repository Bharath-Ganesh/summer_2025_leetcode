import heapq
from collections import defaultdict
from typing import List


class Twitter:
    """
        101 -> tweet1
        /     \
        102   103
        tweet2 tweet3
        101 ->       102, 103
        followeeId   followerId

        Tweets How do I rank the tweets? Static class variable
        TWEET IDS - 1
        101 -> [(3, tweet1)] // Top 10
        102 -> [(1, tweet2)] // Top 10
        103 -> [(2, tweet3)] // Top 10
    """

    TWEET_ID_ORDER = 1

    def __init__(self):
        # userId -> set of followeeIds
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((Twitter.TWEET_ID_ORDER, tweetId))
        Twitter.TWEET_ID_ORDER += 1 # Accessing class level variable

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet IDs in the user's news feed.
        Includes the user's own tweets and those of people they follow.
        """
        heap: List[tuple[int, int]] = []
        # consider the user themself plus everyone they follow
        users = self.followers[userId] | {userId}
        for uid in users:
            # only need up to the last 10 tweets from each
            for ts, tid in self.tweets[uid][-10:]:
                # use a min-heap of size at most 10 with (timestamp, tweetId)
                heapq.heappush(heap, (ts, tid))
                if len(heap) > 10:
                    heapq.heappop(heap)

        # extract in reverse order to get most-recent first
        res = [tid for (_, tid) in heapq.nlargest(len(heap), heap)]
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """followerId starts following followeeId."""
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """followerId stops following followeeId."""
        self.followers[followerId].discard(followeeId)


if __name__ == "__main__":
    twitter = Twitter()

    a = [1,2,3 ]
    print(a[-9:])
    # User 1 posts a new tweet (id = 5).
    twitter.postTweet(1, 5)

    # User 1's news feed should return [5].
    print(twitter.getNewsFeed(1))  # [5]

    # User 1 follows user 2.
    twitter.follow(1, 2)

    # User 2 posts a new tweet (id = 6).
    twitter.postTweet(2, 6)

    # User 1's news feed should return [6, 5].
    print(twitter.getNewsFeed(1))  # [6, 5]

    # User 1 unfollows user 2.
    twitter.unfollow(1, 2)

    # User 1's news feed should now return only [5].
    print(twitter.getNewsFeed(1))  # [5]
