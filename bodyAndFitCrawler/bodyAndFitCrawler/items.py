# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BodyandfitcrawlerItem(scrapy.Item):
    allergens = scrapy.Field()
    category = scrapy.Field()
    description_long = scrapy.Field()
    description_short = scrapy.Field()
    flavours = scrapy.Field()
    large_image_url = scrapy.Field()
    name = scrapy.Field()
    nutrition = scrapy.Field()
    prices = scrapy.Field()
    sizes = scrapy.Field()
    small_image_url = scrapy.Field()
    url = scrapy.Field()