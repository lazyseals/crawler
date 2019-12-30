# -*- coding: utf-8 -*-
import scrapy, re
from scrapy.exceptions import CloseSpider
from scrapy.http import Request
from bs4 import BeautifulSoup

from bodyAndFitCrawler.items import BodyandfitcrawlerItem

#
# Execute crawler: scrapy crawl bodyAndFitSpider -o bodyAndFit.json
#
# Execute shell: scrapy shell "<url>"
#

#
# TODO:
# - Follow pagination to next sites
# - Add more categories
# - Add dynamic rendered content
# - Add products to database
#

class BodyandfitspiderSpider(scrapy.Spider):
    # Unique spider name
    name = 'bodyAndFitSpider'

    # All urls to scrape
    # First url: milchproteine
    start_urls = ['https://www.bodyandfit.com/de-de/Produkte/Protein/Milchproteine/c/2']

    # Current page for pagination
    page = 0
    
    # Parse method invoked by scrapy
    def parse(self, response):

        # Products on product list page
        products = response.xpath('//article[@class="product-slab"]')

        # Check if products available
        if not products:
            raise CloseSpider("No more products!")

        # Iterate each product on site
        for product in products:

            # Item containing product information
            item = BodyandfitcrawlerItem()

            # All information available on product page
            name = product.xpath('.//div[@class="product-slab__wrapper"]/div[@class="product-slab__title"]').extract()
            name = self.cleanText(self.parseText(self.listToStr(name)))

            imageUrl = product.xpath('.//a[@class="product-slab__gallery"]').extract()
            imageUrl = self.cleanText(self.parseImg(self.listToStr(imageUrl)))

            description_short = product.xpath('.//div[@class="product-slab__wrapper"]/'
                                              'div[@class="product-slab__information"]').extract()
            description_short = self.cleanText(self.parseText(self.listToStr(description_short)))

            # Store information per item
            item['name'] = ''.join(name).strip()
            item['imageUrl'] = ''.join(imageUrl).strip()
            item['description_short'] = ''.join(description_short).strip()

            # Follow each product on its detail page
            detail_page = product.xpath('.//a[@class="product-slab__gallery"]/@href').get()
            if detail_page is not None:
                yield response.follow(detail_page, callback=self.parseItemDetail, meta={'item': item})

        # Follow paginiation to next sites
        self.page += 1
        next_page_url = response.request.url + "?text=%%3Arelevance%%3A&page=%d" % self.page
        yield Request(url=next_page_url, callback=self.parse)


    # Parse item detail
    def parseItemDetail(self, response):

        item = response.meta['item']

        # All information available on product page
        description_long = response.xpath('//h2[@class="product-overview__info-header"]').extract()
        description_long = self.cleanText(self.parseText((self.listToStr(description_long))))

        naehrwert = response.xpath('//section[@id="tabNutrition"]').extract()
        naehrwert = self.cleanText(self.parseImg((self.listToStr(naehrwert))))

        ''' Dynamically rendered
        size_to_price = response.xpath('//select[@id="variant-selector-primary"]').extract()
        size_to_price = self.cleanText(self.parseSelect((self.listToStr(size_to_price))))
        geschmack = response.xpath('//select[@id="variant-selector-secondary"]').extract()
        geschmack = self.cleanText(self.parseSelect((self.listToStr(geschmack))))
        size_to_price_to_geschmack = 
        '''

        # Store information per item
        item['description_long'] = ''.join(description_long).strip()
        item['naehrwert'] = ''.join(naehrwert).strip()
        # item['size_to_price_to_geschmack'] = ''.join(size_to_price).strip()

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

    def parseSelect(self, str):
        soup = BeautifulSoup(str, 'html.parser')
        return [str(x.text) for x in soup.find_all('option')]

    # Cleans extracted information
    def cleanText(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        text = soup.get_text();
        text = re.sub("( +|\n|\r|\t|\0|\x0b|\xa0|\xbb|\xab)+", ' ', text).strip()
        return text

    # Creates json with matching of sizes to prices to flavours
    #
    # Example Output:
    # [{
    #   "size": 750g,
    #   "price": 6.5€,
    #   "flavours": [banana, schoko, vanilla]
    # }]
    #
    # Size_to_Price: [X_1 gramm (Y_1 shakes): Z_1€, X_2 gramm (Y_2 shakes): Z_2€]
    def splitSizesAndPrices(self, size_to_price, flavours):

        i = 0
        output = []
        unified = {}

        for sizePrice in size_to_price:

            size = sizePrice.split(" ")[0]  # X
            price = sizePrice.split(" ")[4]  # Z

            unified["size"] = size
            unified["price"] = price
            unified["flavours"] = flavours[i]

            output.append(unified)
            i += 1

        return output
