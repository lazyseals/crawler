# -*- coding: utf-8 -*-
import scrapy, re
from scrapy.exceptions import CloseSpider
from scrapy.http import Request
from scrapy_splash import SplashRequest
from scrapy.utils.response import open_in_browser
from scrapy.http.response.html import HtmlResponse
from scrapy.shell import inspect_response
from bs4 import BeautifulSoup

from bodyAndFitCrawler.items import BodyandfitcrawlerItem

#
# Execute crawler: scrapy crawl bodyAndFitSpider -o bodyAndFit.json
#
# Execute shell with scrapy splash: scrapy shell "http://localhost:8050/render.html?url=<url>"
#
# Execute shell: scrapy shell "<url>"
#
# Execute splash renderer: docker run -p 8050:8050 scrapinghub/splash --max-timeout 3600
#
# docker stop xenodochial_northcutt
#


class BodyandfitspiderSpider(scrapy.Spider):
    # Unique spider name
    name = 'bodyAndFitSpider'

    # Start url
    start_urls = ['https://www.bodyandfit.com/de-de/Produkte/Protein/Milchproteine/c/2']

    # basic url
    url = "https://www.bodyandfit.com"

    # Current page for pagination
    page = 0

    # Allowed categories
    allowed = ['Protein', 'Sportnahrung', 'Food & Snacks', 'Abnehmen', 'Gesundheit']

    # Lua script for splash
    lua_script = """
        function main(splash)
            assert(splash:go(splash.args.url))
            counter = 1
            
            while not splash:select('#variant-selector-primary') do
                print(counter)
                splash:wait(0.1)
                counter = counter + 1
                if counter >= 20 then 
                    break 
                end
            end
            
            return {html=splash:html()}
        end
        """

    # Parse method invoked by scrapy TODO: move to start_request
    '''def parse(self, response):

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
                        yield SplashRequest(url=url, callback=self.parse_category, endpoint='render.html')'''

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html')

    # Parse category
    def parse(self, response):
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
            item = self.parse_product(response, product, item)

            # Follow each product on its detail page
            detail_page = product.xpath('.//a[@class="product-slab__gallery"]/@href').get()
            if detail_page:
                url = self.url + detail_page
                yield SplashRequest(url=url, callback=self.parse_item_detail, endpoint='execute',
                                    meta={'item': item}, args={'lua_source': self.lua_script})

        # Follow pagination to next sites
        self.page += 1
        next_page_url = response.request._original_url + "?text=%%3Arelevance%%3A&page=%d" % self.page
        yield SplashRequest(url=next_page_url, callback=self.parse, endpoint='render.html')

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
        ht = HtmlResponse(url=response.url, body=response.body, encoding="utf-8", request=response.request)

        large_image_url = ht.xpath('//*[contains(@class, "product-gallery")]')
        large_image_url = large_image_url.extract()
        large_image_url = self.clean_text(self.parse_img(self.list_to_str(large_image_url)))

        url = response.request._original_url

        name = response.xpath('//*[contains(@class, "product-details__name")]').extract()
        name = self.clean_text(self.parse_text(self.list_to_str(name)))

        nutrition = response.xpath('//section[@id="tabNutrition"]').extract()
        nutrition = self.clean_text(self.parse_img(self.list_to_str(nutrition)))

        description_long = response.xpath('//*[contains(@class, "product-overview__info-text")]').extract_first()

        if not description_long:
            description_long = item['description_short']
        else:
            description_long = self.clean_text(self.parse_text(self.list_to_str(description_long)))

        size_to_price = response.xpath('//select[@id="variant-selector-primary"]').extract()

        if not size_to_price:
            sizes = response.xpath('//*[contains(@class, "variant-selector__selector--primary")]').extract()
            sizes = self.clean_text(self.parse_text(self.list_to_str(sizes)))
            prices = response.xpath('//*[contains(@class, "product-price__value")]').extract_first()
            prices = self.clean_text(self.parse_text(self.list_to_str(prices)))
            flavours = 'Neutral'
        else:
            size_to_price = self.parse_select(self.list_to_str(size_to_price))
            sizes, prices = self.get_sizes_and_prices_from_select(size_to_price)
            flavours = response.xpath('//select[@id="variant-selector-secondary"]').extract()
            flavours = self.parse_select(self.list_to_str(flavours))

        item['name'] = ''.join(name).strip()
        item['large_image_url'] = ''.join(large_image_url).strip()
        item['description_long'] = ''.join(description_long).strip()
        item['nutrition'] = ''.join(nutrition).strip()
        item['allergens'] = ''.join(nutrition).strip()  # Allergens are stored in nutrition picture
        item['sizes'] = sizes
        item['prices'] = prices
        item['flavours'] = flavours
        item['url'] = ''.join(url).strip()

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
        size_to_price.pop(0)
        for size_price in size_to_price:
            sizes.append(size_price.split(" ")[0] + " " + size_price.split(" ")[1])
            prices.append(size_price.split(" ")[5] + " " + size_price.split(" ")[6])
        return sizes, prices
