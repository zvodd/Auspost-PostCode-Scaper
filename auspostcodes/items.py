# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AuspostcodesItem(scrapy.Item):
    # define the fields for your item here like:
    suburb = scrapy.Field()
    url = scrapy.Field()

class PostcodeItem(scrapy.Item):
	suburb = scrapy.Field()
	postcode = scrapy.Field()
	state = scrapy.Field()