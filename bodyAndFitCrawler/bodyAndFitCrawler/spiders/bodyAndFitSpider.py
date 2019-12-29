# -*- coding: utf-8 -*-
import scrapy, re
from bs4 import BeautifulSoup

from bodyAndFitCrawler.items import BodyandfitcrawlerItem

class BodyandfitspiderSpider(scrapy.Spider):
    # Unique spider name
    name = 'bodyAndFitSpider'

    # All urls to scrape
    # First url: milchproteine
    start_urls = ['https://www.bodyandfit.com/de-de/Produkte/Protein/Milchproteine/c/2']
    
    # Parse method invoked by scrapy
    def parse(self, response):
        # Item containing product information
        item = BodyandfitcrawlerItem()

        # Iterate each product on site
        for product in response.xpath('//article[@class="product-slab"]'):

            # All information available on product page
            name = product.xpath('.//div[@class="product-slab__wrapper"]/div[@class="product-slab__title"]').extract()
            name = self.cleanText(self.parseText(self.listToStr(name)))
            
            imageUrl = product.xpath('.//a[@class="product-slab__gallery"]').get()
            imageUrl = self.cleanText(self.parseImg(self.listToStr(imageUrl)))
            
            description_short = product.xpath('.//div[@class="product-slab__wrapper"]/div[@class="product-slab__information"]').extract()
            description_short = self.cleanText(self.parseText(self.listToStr(description_short)))
            
            # Store information per item
            item['name'] = ''.join(name).strip()
            item['imageUrl'] = ''.join(imageUrl).strip()
            item['description_short'] = ''.join(description_short).strip()

            # Yield each item
            yield item

    # Returns all strings in list
    def listToStr(self, MyList):
        dumm = ""
        for i in MyList: dumm = "{0}{1}".format(dumm, i)
        return dumm

    # Parses text from html element
    # Example: <a>Some Text</a> => Some Text
    def parseText(self, str):
        soup = BeautifulSoup(str, 'html.parser')
        return re.sub(" +|\n|\r|\t|\0|\x0b|\xa0", ' ', soup.get_text()).strip()

    # Parses img src from html elements
    # Example: <img src="/some/path"> => /some/path
    def parseImg(self, str):
        soup = BeautifulSoup(str, 'html.parser')
        images = soup.find_all('img')
        for img in images:
            return img['src']

    # Cleans extracted information
    def cleanText(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        text = soup.get_text();
        text = re.sub("( +|\n|\r|\t|\0|\x0b|\xa0|\xbb|\xab)+", ' ', text).strip()
        return text
