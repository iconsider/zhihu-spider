# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class UserItem(scrapy.Item):
    username = scrapy.Field()
    userId = scrapy.Field()
    followers = scrapy.Field()
    following = scrapy.Field()
    title = scrapy.Field()
