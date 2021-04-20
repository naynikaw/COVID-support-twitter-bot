import tweepy

keys = {
    'CONSUMER_API_KEY': '',
    'CONSUMER_API_SECRET_KEY': '',
    'ACCESS_TOKEN': '',
    'ACCESS_TOKEN_SECRET': ''
}

def handler(event, context):
    auth = tweepy.OAuthHandler(
        keys['CONSUMER_API_KEY'],
        keys['CONSUMER_API_SECRET_KEY']
    )
    auth.set_access_token(
        keys['ACCESS_TOKEN'],
        keys['ACCESS_TOKEN_SECRET']
    )
    api = tweepy.API(auth)
    mentions = api.mentions_timeline()
    for mention in mentions:
        if mention.in_reply_to_status_id is not None:
            parent_tweet = api.get_status(mention.in_reply_to_status_id)
            try:
                if not parent_tweet.retweeted:
                    parent_tweet.retweet()
            
            except:
                    print("Error on retweeting parent")
            return
                  
        if not mention.retweeted:
            try:
                mention.retweet()
            except:
                print("Error on retweet")
        return 
