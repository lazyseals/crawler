# -*- coding: utf-8 -*-
import scrapy, re
from scrapy.exceptions import CloseSpider
from scrapy.http import Request
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup

from bodyAndFitCrawler.items import BodyandfitcrawlerItem

#
# Execute crawler: scrapy crawl bodyAndFitSpider -o bodyAndFit.json
#
# Execute shell: scrapy shell "<url>"
#
# Execute splash renderer: docker run -p 8050:8050 scrapinghub/splash
#

#
# TODO:
# - Add dynamic rendered content
# - Add products to database
#


class BodyandfitspiderSpider(scrapy.Spider):
    # Unique spider name
    name = 'bodyAndFitSpider'

    # Start url
    start_urls = ['https://www.bodyandfit.com/de-de']

    # basic url
    url = "https://www.bodyandfit.com"

    # Current page for pagination
    page = 0

    # Allowed categories
    allowed = ['Protein', 'Sportnahrung', 'Food & Snacks', 'Abnehmen', 'Gesundheit']

    # Parse method invoked by scrapy
    def parse(self, response):

        # Categories from navbar
        main_categories = response.xpath('//li[contains(@class, "mega-nav__category-list-item") '
                                         'and contains(@class, "mega-nav__primary-category")]')

        # Check if categories available
        if not main_categories:
            raise CloseSpider('No more categories')

        # Iterate each category
        for main_category in main_categories:

            main_category_name = main_category.xpath('./div/a').extract()
            main_category_name = self.clean_text(self.parse_text(self.list_to_str(main_category_name)))

            if main_category_name in self.allowed:

                sub_categories = main_category.xpath('.//li[contains(@class, "mega-nav__category-list-item") '
                                                     'and not(contains(@class, "mega-nav__primary-category"))]')

                for sub_category in sub_categories:

                    category_page = sub_category.xpath('./div/a/@href').get()

                    if category_page:
                        url = self.url + category_page
                        self.page = 0
                        yield SplashRequest(url=url, callback=self.parse_category, endpoint='render.html')

    # Parse category
    def parse_category(self, response):
        # Products on product list page
        products = response.xpath('//article[@class="product-slab"]')

        # Check if products available
        if not products:
            return

        # Iterate each product on site
        for product in products:

            # item per product
            item = BodyandfitcrawlerItem()

            # store product information in item
            self.parse_product(response, product, item)

            # Follow each product on its detail page
            detail_page = product.xpath('.//a[@class="product-slab__gallery"]/@href').get()
            if detail_page:
                url = self.url + detail_page
                yield SplashRequest(url=url, callback=self.parse_item_detail, endpoint='render.html',
                                    meta={'item': item})

        # Follow pagination to next sites
        self.page += 1
        next_page_url = response.request.url + "?text=%%3Arelevance%%3A&page=%d" % self.page
        yield SplashRequest(url=next_page_url, callback=self.parse_category, endpoint='render.html')

    def parse_product(self, response, product, item):
        small_image_url = product.xpath('.//a[@class="product-slab__gallery"]').extract()
        small_image_url = self.clean_text(self.parse_img(self.list_to_str(small_image_url)))

        description_short = product.xpath('.//div[@class="product-slab__wrapper"]/'
                                          'div[@class="product-slab__information"]').extract()
        description_short = self.clean_text(self.parse_text(self.list_to_str(description_short)))

        category = response.xpath('//h1[contains(@class, "heading--large")]').extract()
        category = self.clean_text(self.parse_text(self.list_to_str(category)))

        item['small_image_url'] = ''.join(small_image_url).strip()
        item['description_short'] = ''.join(description_short).strip()
        item['category'] = ''.join(category).strip()

        return item

    # Parse item detail
    def parse_item_detail(self, response):

        item = response.meta['item']

        large_image_url = response.xpath('//*[contains(@class, "amp-slide")]').extract()
        large_image_url = self.clean_text(self.parse_img(self.list_to_str(large_image_url)))

        name = response.xpath('//*[contains(@class, "product-details__name")]').extract()
        name = self.clean_text(self.parse_text(self.list_to_str(name)))

        description_long = response.xpath('//*[contains(@class, "product-overview__info-text")]').extract()
        description_long = self.clean_text(self.parse_text(self.list_to_str(description_long)))

        nutrition = response.xpath('//section[@id="tabNutrition"]').extract()
        nutrition = self.clean_text(self.parse_img(self.list_to_str(nutrition)))

        size_to_price = response.xpath('//select[@id="variant-selector-primary"]').extract()

        if not size_to_price:
            sizes = response.xpath('//*[contains(@class, "variant-selector__selector")]').extract()
            sizes = self.clean_text(self.parse_text(self.list_to_str(sizes)))
            prices = response.xpath('//*[contains(@class, "variant-selector__price")]').extract()
            prices = self.clean_text(self.parse_text(self.list_to_str(prices)))
            flavours = 'Neutral'
        else:
            size_to_price = self.clean_text(self.parse_select(self.list_to_str(size_to_price)))
            sizes, prices = self.get_sizes_and_prices_from_select(size_to_price)
            flavours = response.xpath('//select[@id="variant-selector-secondary"]').extract()
            flavours = self.clean_text(self.parse_select(self.list_to_str(flavours)))

        item['name'] = ''.join(name).strip()
        item['large_img_url'] = ''.join().strip()
        item['description_long'] = ''.join(description_long).strip()
        item['nutrition'] = ''.join(nutrition).strip()
        item['allergens'] = ''.join(nutrition).strip()  # Allergens are stored in nutrition picture
        item['sizes'] = ''.join(sizes).strip()
        item['prices'] = ''.join(prices).strip()
        item['flavours'] = ''.join(flavours).strip()

        yield item

    # Returns all strings in list
    @staticmethod
    def list_to_str(my_list):
        dummy = ""
        for i in my_list:
            dummy = "{0}{1}".format(dummy, i)
        return dummy

    # Parses text from html element
    # Example: <a>Some Text</a> => Some Text
    @staticmethod
    def parse_text(string):
        soup = BeautifulSoup(string, 'html.parser')
        return re.sub(" +|\n|\r|\t|\0|\x0b|\xa0", ' ', soup.get_text()).strip()

    # Parses img src from html elements
    # Example: <img src="/some/path"> => /some/path
    @staticmethod
    def parse_img(string):
        soup = BeautifulSoup(string, 'html.parser')
        images = soup.find_all('img')
        for img in images:
            return img['src']

    # Parses text from options from select element
    @staticmethod
    def parse_select(string):
        soup = BeautifulSoup(string, 'html.parser')
        return [str(x.text) for x in soup.find_all('option')]

    # Cleans extracted information
    @staticmethod
    def clean_text(text):
        soup = BeautifulSoup(text, 'html.parser')
        text = soup.get_text()
        text = re.sub("( +|\n|\r|\t|\0|\x0b|\xa0|\xbb|\xab)+", ' ', text).strip()
        return text

    # Extracts sizes and prices from size to price string
    # Input list of following string types: 750 gram (26  shakes): 12,50 €
    @staticmethod
    def get_sizes_and_prices_from_select(size_to_price):
        sizes = []
        prices = []
        for size_price in size_to_price:
            sizes.append(size_price.split(" ")[0])
            prices.append(size_price.split(" ")[4])
        return sizes, prices
