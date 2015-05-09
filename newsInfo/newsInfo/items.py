# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class NewsinfoItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()			#新闻标题
    content = Field()		#新闻内容摘要
    publishTime = Field()	#发布时间
    detailLink = Field()	#详情页链接
