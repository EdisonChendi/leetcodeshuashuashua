import unittest
from typing import List
from pprint import pprint

'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''

import collections
import time
import functools

@functools.total_ordering
class Tweet:

    ID = 1

    @classmethod
    def create(cls, user_id, tweet_text):
        return Tweet(user_id, tweet_text)

    def __init__(self, user_id, text) -> None:
        self.id = Tweet.ID
        self.user_id = user_id
        self.text = text
        self.create_time = time.time()
        Tweet.ID += 1
    
    def __gt__(self, other):
        return self.create_time < other.create_time

    def __eq__(self, other):
        return self.create_time == other.create_time
    
    def __repr__(self):
        return f"id: {self.id}, userid: {self.user_id}, text: {self.text}, create_time: {self.create_time}"

import heapq
def k_merge_sort(tweets, n):
    res = []
    h = [] # heap

    pointers = [0]*len(tweets)

    h = [(tweets[i][p],i) for i,p in enumerate(pointers) if p < len(tweets[i])]
    heapq.heapify(h)


    while h and len(res) < n:
        _, i = heapq.heappop(h)
        res.append(tweets[i][pointers[i]])
        pointers[i] += 1
        if pointers[i] < len(tweets[i]):
            heapq.heappush(h, (tweets[i][pointers[i]], i))
    return res
    
class MiniTwitter:
    
    def __init__(self):
        # do intialization if necessary
        self.following = collections.defaultdict(set)
        self.followed = collections.defaultdict(set)
        self.tweets = collections.defaultdict(list)

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    def postTweet(self, user_id, tweet_text):
        # write your code here
        self.follow(user_id, user_id)
        tweet = Tweet.create(user_id, tweet_text)
        self.tweets[user_id].append(tweet)
        return tweet

    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    def getNewsFeed(self, user_id):
        # write your code here
        # use pull model
        # read fan out
        # algorithm: k-merge sort
        following = self.following[user_id]
        all_tweets = [self.getTimeline(f) for f in following]
        return k_merge_sort(all_tweets, 10)

    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        # write your code here
        return self.tweets[user_id][-10:][::-1]

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        # write your code here
        self.following[from_user_id].add(to_user_id)
        self.followed[to_user_id].add(from_user_id)

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        # write your code here
        self.following[from_user_id].remove(to_user_id)
        self.followed[to_user_id].remove(from_user_id)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        twitter = MiniTwitter()
        print(twitter.postTweet(1, "LintCode is Good!!!"))
        print(twitter.getNewsFeed(1))
        print(twitter.getTimeline(1))
        print(twitter.follow(2, 1))
        print(twitter.postTweet(1, "LintCode is best!!!"))
        print(twitter.getNewsFeed(2))
        print(twitter.unfollow(2, 1))
        print(twitter.getNewsFeed(2))

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
