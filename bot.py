import logging.config
import time

import followers
import news_api_auth
import news_grabber
import tweets
import twitter_api_auth

INTERVAL = 60 * 30  # tweet every 30 minutes

logging.config.fileConfig('logging.config')
logger = logging.getLogger(__name__)

news_api = news_api_auth.create_api()
news_grabber = news_grabber.NewsGrabber(news_api)

tw_api = twitter_api_auth.create_api()
tw_handler = tweets.TweetsHandler(tw_api)
followers_handler = followers.FollowersHandler(tw_api)


def tweet_something_about(keyword):
    news = news_grabber.get_news(keyword)
    if len(news) == 0:
        return False
    logger.info('Tweeting about ' + keyword)
    # tw_handler.post_new_tweet(news[0].title, news[0].url)
    for n in news:
        tw_handler.post_new_tweet(n.title, n.url)
        time.sleep(1000)


while True:
    # follow new followers
    followers_handler.follow_followers()

    # check for bitcoin news and tweet about it
    tweet_something_about('bitcoin')

    # check for cryptocurrency news and tweet about it
    tweeted = tweet_something_about('cryptocurrency')

    logger.info('going to sleep now...')
    time.sleep(INTERVAL)
