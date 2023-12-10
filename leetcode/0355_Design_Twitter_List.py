"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 
Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 
Constraints:

1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 104
All the tweets have unique IDs.
At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
"""
import heapq

class Twitter:

    def __init__(self):
        self.users_tweets = {}
        self.users_follows = {}
        self.post_id = {}
        self.post_date = 0

    # def postTweet(self, userId: int, tweetId: int) -> None:
    def postTweet(self, userId, tweetId):
        if userId not in self.users_tweets:
            self.users_tweets[userId] = []
        self.post_date += 1
        self.users_tweets[userId].append(self.post_date)
        self.post_id[self.post_date] = tweetId

    # def getNewsFeed(self, userId: int) -> List[int]:
    def getNewsFeed(self, userId):
        possible_users_id = {}
        if userId in self.users_tweets:
            possible_users_id[userId] = -1

        if userId in self.users_follows:
            for user in self.users_follows[userId]:
                if user in self.users_tweets:
                    possible_users_id[user] = -1
        posts = []

        while possible_users_id and len(posts) < 10:
            newest_user = None
            for user in possible_users_id:
                if newest_user == None:
                    newest_user = user
                elif self.users_tweets[user][possible_users_id[user]] > self.users_tweets[newest_user][possible_users_id[newest_user]]:
                    newest_user = user
            posts.append(self.post_id[self.users_tweets[newest_user][possible_users_id[newest_user]]])

            if len(self.users_tweets[newest_user]) + possible_users_id[newest_user] > 0:
                possible_users_id[newest_user] -= 1
            else:
                del possible_users_id[newest_user]

        return posts

    # def follow(self, followerId: int, followeeId: int) -> None:
    def follow(self, followerId, followeeId):
        if followerId not in self.users_follows:
            self.users_follows[followerId] = set()

        self.users_follows[followerId].add(followeeId)

    # def unfollow(self, followerId: int, followeeId: int) -> None:
    def unfollow(self, followerId, followeeId):
        if followerId in self.users_follows:
            self.users_follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

def main():
    solution = []
    twitter = Twitter()
    solution.append(twitter.postTweet(1, 1))
    solution.append(twitter.getNewsFeed(1))
    solution.append(twitter.follow(2, 1))
    solution.append(twitter.getNewsFeed(2))
    solution.append(twitter.unfollow(2, 1))
    solution.append(twitter.getNewsFeed(2))
    
    print(solution)


if __name__ == "__main__":
    main()