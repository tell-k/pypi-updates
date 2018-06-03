# -*- coding: utf-8 -*-
"""
    pypi_updates.bot
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Bot for PyPI Recent Updates

    :author: tell-k <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
import os

import kuroko
import tweepy
import feedparser
import pylibmc
from dateutil import parser
from dateutil.relativedelta import relativedelta

RSS_URL = "https://pypi.org/rss/updates.xml"
TWEET_MAX_LENGTH = 130
ELIPSIS = "..."

NG_WORDS = [
    'kissanime',
]


def is_valid_message(msg):
    for ng_word in NG_WORDS:
        if ng_word in msg:
            return False
    return True


class PypiUpdatesBot(kuroko.Bot):

    @property
    def tweepy_api(self):
        if hasattr(self, "_tweepy_api"):
            return self._tweepy_api
        auth = tweepy.OAuthHandler(
            os.getenv("TWITTER_CONSUMER_KEY"),
            os.getenv("TWITTER_CONSUMER_SECRET"),
        )
        auth.set_access_token(
            os.getenv("TWITTER_ACCESS_KEY"),
            os.getenv("TWITTER_ACCESS_SECRET")
        )
        self._tweepy_api = tweepy.API(auth)
        return self._tweepy_api

    @property
    def memcache(self):
        if hasattr(self, "_memcache"):
            return self._memcache
        self._memcache = pylibmc.Client(
            [os.getenv("MEMCACHIER_SERVERS")],
            username=os.getenv("MEMCACHIER_USERNAME"),
            password=os.getenv("MEMCACHIER_PASSWORD"),
            binary=True
        )
        return self._memcache


    @kuroko.crontab('*/1 * * * *')
    def update_status(self):
        print('Start update status')
        rss = feedparser.parse(RSS_URL)
        # skip non feed items.
        if not rss or not rss['items']:
            msg = "Can't parse RSS: {}".format(RSS_URL)
            self.log.warning(msg)
            print(msg)
            return

        latest_published = self.memcache.get("latest_published")
        if not latest_published:
            dt = parser.parse(rss['items'][-1]['published'])
            dt -= relativedelta(seconds=1)
            latest_published = dt.strftime('%Y%m%d%H%M%S')
            self.memcache.set("latest_published", latest_published)

        msg = "latest_published => {}".format(latest_published)
        self.log.info(msg)
        print(msg)
        tmp_latest = latest_published
        for item in rss['items']:
            published = parser.parse(
                item['published']
            ).strftime('%Y%m%d%H%M%S')

            # skip old feed.
            if int(published) <= int(latest_published):
                continue

            title = item['title']
            real_len = len(title) + len(item['link']) + 1
            if TWEET_MAX_LENGTH < real_len:
                truncate_len = real_len - TWEET_MAX_LENGTH + len(ELIPSIS)
                title = title[:-truncate_len] + ELIPSIS

            # tweet
            message = u"{} {}".format(title, item['link'])
            self.log.info(message)
            print(message)
            try:
                if is_valid_message(message):
                    self.tweepy_api.update_status(message)

                # update latest_published cache
                if tmp_latest < published:
                    tmp_latest = published
                    self.memcache.set("latest_published", published)

            except tweepy.TweepError as e:
                self.log.error(e.message)
                print(e.message)

        print('End update status')
