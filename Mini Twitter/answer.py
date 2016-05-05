'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''
class MiniTwitter:
    def __init__(self):
        # initialize your data structure here.
        self.all_tweet = []
        self.all_friend = []
        self.time = 0

    # @param {int} user_id
    # @param {str} tweet
    # @return {Tweet} a tweet
    def postTweet(self, user_id, tweet_text):
        # Write your code here
        self.time = self.time+1
        tweet = Tweet.create(user_id, tweet_text)
        self.all_tweet.append({'id': tweet,'time': self.time ,'user_id': user_id })
        return tweet

    # @param {int} user_id
    # return {Tweet[]} 10 new feeds recently
    # and sort by timeline
    def getNewsFeed(self, user_id):
        # Write your code here
        friend = []
        tweet = []
        friend.append(user_id)
        for i in self.all_friend:
            if(i[0] == user_id):
                friend.append(i[1])
        for i in reversed(self.all_tweet):
            if(i['user_id'] in friend):
                tweet.append(i['id'])
        return tweet[0:10]     
        
    # @param {int} user_id
    # return {Tweet[]} 10 new posts recently
    # and sort by timeline
    def getTimeline(self, user_id):
        # Write your code here
        self_tweet = []
        for i in reversed(self.all_tweet):
            if(i['user_id'] == user_id):
                self_tweet.append(i['id'])
        return  self_tweet[0:10]

    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id follows to_user_id
    def follow(self, from_user_id, to_user_id):
        # Write your code here
        self.all_friend.append((from_user_id, to_user_id))

    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id unfollows to_user_id
    def unfollow(self, from_user_id, to_user_id):
        # Write your code here
        self.all_friend.remove((from_user_id, to_user_id))
