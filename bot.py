# -*- coding: utf-8 -*-
"""
    PyPI Recent Updates Twitter bot
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
import os

import kuroko
import tweepy
import feedparser
import pylibmc
import bitlyapi
from dateutil import parser

RSS_URL = "https://pypi.python.org/pypi?:action=rss"
TWEET_MAX_LENGTH = 140


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

    @property
    def bitly_api(self):
        if hasattr(self, "_bitly_api"):
            return self._bitly_api
        self._bitly_api = bitlyapi.BitLy(
            os.getenv("BITLY_USERNAME"),
            os.getenv("BITLY_API_KEY")
        )
        return self._bitly_api

    def _to_string(self, dt):
        return parser.parse(dt).strftime('%Y%m%d%H%M%S')

    @kuroko.crontab('*/1 * * * *')
    def update_status(self):

        rss = feedparser.parse(RSS_URL)
        # skip non feed items.
        if not rss['items']:
            return

        latest_published = self.memcache.get("latest_published")
        if not latest_published:
            latest_published = self._to_string(rss['items'][0]['published'])
            self.memcache.set("latest_published", latest_published)

        self.log.info("latest_published => {}".format(latest_published))

        tmp_published = latest_published
        for item in rss['items']:
            published = self._to_string(item['published'])

            # skip old feed.
            if int(latest_published) >= int(published):
                continue

            # shorten url
            try:
                res = self.bitly_api.shorten(longUrl=item['link'])
                url = res['url']
            except bitlyapi.bitly.APIError as e:
                self.log.error(e)
                url = item['link']

            # truncate description text.
            must_len = len(item['title']) + len(url)
            remain_len = TWEET_MAX_LENGTH - must_len
            desc = item['description']
            if remain_len < len(desc):
                desc = desc[:remain_len - 6] + '..'

            message = "{}: {} {}".format(item['title'], desc, url)
            self.log.info(message)
            try:
                self.tweepy_api.update_status(message)
            except tweepy.TweepError as e:
                self.log.error(e.message)

            if int(tmp_published) < int(published):
                tmp_published = published

        # update latest_published
        if int(tmp_published) > int(latest_published):
            self.memcache.set("latest_published", tmp_published)


if __name__ == "__main__":

    bot = PypiUpdatesBot()
    bot.start()
