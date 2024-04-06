import tweepy
from src.segredinho import *


def get_trends(woe_id: int) -> list[dict[literal, any]]:

    auth = tweepy.OAuthHandler(consumer_key=API_KEY, consumer_secret=API_Key_Secret)

    auth.set_access_token(Access_Token, Access_Token_Secret)

    api = tweepy.API(auth)

    trends = api.get_place_trends(woe_id)
    
    return [trends for trend in trends]
