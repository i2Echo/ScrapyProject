#--coding: utf-8--

from scrapy.spider import Spider
from scrapy.selector import Selector
# from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.contrib.linkextractors import LinkExtractor
# import re
from scrapy.spider import Spider
import json
from newsInfo.items import *

class newsInfoSpider(Spider):

    name = "newsInfo"
    url_list = []
    for page in xrange(1,101):
        url = 'http://zhannei.baidu.com/cse/search?q=%E5%B0%BC%E6%B3%8A%E5%B0%94%E5%9C%B0%E9%9C%87&p=' + str(page) + '&s=16378496155419916178&entry=1&area=2'
        url_list.append(url)
    start_urls = url_list

    def parse(self, response):

        sel = Selector(response)
        items = []

        news_list = sel.xpath("//div[@class='result f s0']")

        for news in news_list:
            item = NewsinfoItem()  
            item['title'] = news.xpath("./h3/a").xpath('string(.)').extract()[0].strip()
            item['detailLink'] = news.xpath("./h3/a/@href").extract()[0]
            item['content'] = news.xpath(".//div[@class='c-abstract']").xpath('string(.)').extract()[0].strip()
            item['publishTime'] = news.xpath(".//span[@class='c-showurl']/text()").extract()[0][-9:].strip()
            items.append(item)

        return items

