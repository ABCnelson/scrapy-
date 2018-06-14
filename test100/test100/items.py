# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ShushanItem(scrapy.Item):
    #分类
    category = scrapy.Field()
    #名称
    name = scrapy.Field()




