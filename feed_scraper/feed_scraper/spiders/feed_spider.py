# -*- coding: utf-8 -*-

import scrapy

import feedparser

from scrapy.http import Request

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class FeedItem(scrapy.Item):
  url = scrapy.Field()

class FeedSpider(CrawlSpider):
  name = "feed_spider"
  allowed_domains = [ "kurtmckee.livejournal.com" ]
  start_urls = [ "http://kurtmckee.livejournal.com/"]

# TODO: make init work
#  def __init__(self, *args, **kwargs):
#    super(FeedSpider, self).__init__(*args, **kwargs)
#    start_urls = kwargs.get('start_urls').split(',')

  rules = (
        Rule(LinkExtractor(allow=('.*', )), callback='parse_link'),
    )

  def parse_link(self, response):
    try:
      parsed_feed = feedparser.parse(response.url);
      self.log("Feed title: " + parsed_feed.feed.title)
      feedItem = FeedItem()
      feedItem['url'] = response.url
      return feedItem
    except:
      return None
