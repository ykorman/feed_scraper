# -*- coding: utf-8 -*-

# Scrapy settings for feed_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'feed_scraper'

SPIDER_MODULES = ['feed_scraper.spiders']
NEWSPIDER_MODULE = 'feed_scraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'feed_scraper (+http://www.yourdomain.com)'

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'application/rss+xml, application/rdf+xml, application/atom+xml, application/xml, text/xml',
}