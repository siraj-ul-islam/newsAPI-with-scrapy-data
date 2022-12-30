from urllib.request import Request

import scrapy


class GetDataFromGoogleApp(scrapy.Spider):
    name = 'googleapp'
    start_urls = ['https://www.google.com/search?q=EPICOM+play+store']

    def parse(self, response):
        for products in response.css('div.yuRUbf'):
            try:
                yield{
                     'link': products.css('a').attrib['href'],
                }
            except:
                yield {
                    'link': products.css('a').attrib['href'],
                }

