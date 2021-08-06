import pandas as pd
import numpy as np
import string
import re
from collections import Counter
from nltk.corpus import stopwords
from GoogleNews import GoogleNews


def search_article_timeframe():
    yahoo_bucket = []
    google_bucket = []
    seeking_alpha_bucket = []

    google_news = GoogleNews()
    google_news.set_lang('en')
    google_news.set_time_range('07/01/2021', '07/20/2021')
    google_news.set_encode('utf-8')
    google_news.get_news('UCTT')
    google_news.search('UCTT')
    links = google_news.get_links()
    protocol = 'https://'  # appends the protocol if the url if the url is missing it.
    url = [protocol + domain if protocol not in domain else domain for domain in links]
    # yahoo_bucket = [domain for domain in links if 'yahoo' in domain]
    yahoo_bucket = [i for i in url if 'yahoo' in i]
    google_bucket = [i for i in url if 'google' in i]
    seeking_alpha_bucket = [i for i in url if 'seeking alpha' in i]
    print(yahoo_bucket)
    print(google_bucket)
    print(url)


def main():
    search_article_timeframe()


main()
