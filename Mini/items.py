# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MiniItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    
class TestItem(scrapy.Item):
	contactName = scrapy.Field()
	Ps = scrapy.Field()
