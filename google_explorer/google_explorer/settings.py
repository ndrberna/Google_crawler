# -*- coding: utf-8 -*-

# Scrapy settings for google_explorer project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

RETRY_TIMES = 3

DOWNLOAD_DELAY= 1
CONCURRENT_REQUESTS = 16
LOG_ENABLED = False
LOG_LEVEL = "INFO"
BOT_NAME = 'robot'
SCHEDULER = 'scrapy.core.scheduler.Scheduler'
SPIDER_MODULES = ['google_explorer.spiders']
NEWSPIDER_MODULE = 'google_explorer.spiders'

DEFAULT_REQUEST_HEADERS = {
    'Referer': 'http://www.bing.com',
    'Accept':'text/heml,application/xhtml+xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'de',

}

ITEM_PIPELINES = ['google_explorer.pipelines.DuplicatesPipeline']
IMAGES= '/Users/bordoni/.virtualenvs/archivio/'
IMAGES_EXPIRES = 90
DOWNLOADER_MIDDLEWARES = {
		'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
		
    	# Fix path to this module
    	#'google_explorer.randomproxy.RandomProxy': 100,
    	'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'google_explorer.spiders.rotate_useragent.RotateUserAgentMiddleware' :400,
        
    }

PROXY_LIST = '/Users/bordoni/.virtualenvs/Scrapy/google_explorer/google_explorer/list_proxy.txt'
