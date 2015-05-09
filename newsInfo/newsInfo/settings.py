# -*- coding: utf-8 -*-

# Scrapy settings for newsInfo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'newsInfo'

SPIDER_MODULES = ['newsInfo.spiders']
NEWSPIDER_MODULE = 'newsInfo.spiders'

ITEM_PIPELINES = {
    'newsInfo.pipelines.NewsinfoPipeline': 800,
}

#USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'
#DOWNLOAD_TIMEOUT = 15
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'newsInfo (+http://www.yourdomain.com)'
