import sys
import unittest
from GoogleNews import GoogleNews
import article_sentiment
from unittest.mock import MagicMock, Mock
import pytest

mock = Mock()


class TestStringMethods(unittest.TestCase):

    def test_analyze_sentence(self):
        google_news = GoogleNews()
        google_news.set_lang('en')
        google_news.set_time_range('07/01/2021', '07/24/2021')
        google_news.set_encode('utf-8')
        google_news.get_news('UCTT')
        google_news.search('UCTT')
        result = google_news.get_page(1)
        google_news.results()
        google_news.get_texts()
        self.links = google_news.get_links()
        ss = 'http://'
        self.sh = [ss + s for s in self.links]
        self.assertIsNotEqual(self.sh, 0)

    # def test_parse_article(self):
    #    pass

    # def test_lexical_article_analyze(self):
    #   pass

    if __name__ == '__main__':
        unittest.main()