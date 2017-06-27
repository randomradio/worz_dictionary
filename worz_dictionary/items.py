# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WorzRawDictionaryItem(scrapy.Item):
    # define the fields for your item here like:
    source = scrapy.Field()
    word = scrapy.Field()
    raw_html = scrapy.Field()
    error = scrapy.Field()
