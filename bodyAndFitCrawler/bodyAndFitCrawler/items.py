# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BodyandfitcrawlerItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    size_to_price_to_geschmack = scrapy.Field()
    description_short = scrapy.Field()
    description_long = scrapy.Field()
    imageUrl = scrapy.Field()
    allergene = scrapy.Field()
    popularity = scrapy.Field()
    naehrwert = scrapy.Field()
