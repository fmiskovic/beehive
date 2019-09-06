import logging.config
import unittest

from news import news_api_auth
from news.news_grabber import NewsGrabber

logging.config.fileConfig('logging.config')
logger = logging.getLogger('bot')


class NewsGrabberTestCases(unittest.TestCase):
    def setUp(self):
        api = news_api_auth.create_api()
        self.grabber = NewsGrabber(api, logging)

    def tearDown(self) -> None:
        super().tearDown()

    def test_get_crypto_news(self):
        news = self.grabber.get_news('cryptocurrency')
        print('crypto')
        for n in news:
            print(n)
        self.assertTrue(len(news) > 0)

    def test_get_crypto_tech_news(self):
        news = self.grabber.get_news('cryptocurrency', category='technology')
        print('crypto')
        for n in news:
            print(n)
        self.assertTrue(len(news) > 0)

    def test_get_bitcoin_news(self):
        news = self.grabber.get_news('bitcoin')
        print('bitcoin')
        for n in news:
            print(n)
        self.assertTrue(len(news) > 0)

    def test_get_news_non_existing(self):
        news = self.grabber.get_news('fqwsdzx')
        self.assertTrue(len(news) == 0)


if __name__ == '__main__':
    unittest.main()
