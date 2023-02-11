import tweepy


access_token = '1579347585189281792-o40xO1BcTzf3gZsbfKinBfg4xn4toM'
access_token_secret = 'tC8dTWF4uhLJaVIXDw0dkFdrUyvV3C7pGH6dbMSj7Omrj'
consumer_key = '9hXw6rZqo7s4t2TyewATpFgCJ'
consumer_secret = 'fakUoe9ubEDaE4kymOTC4k9pGJQ3stETQnAOXiMjbjGe2CN7Yk'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api.update_status("Just posting for fun")
api.update_status("I am not vadivelu")