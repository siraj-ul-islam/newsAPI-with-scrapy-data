import scrapy
from scrapy import Request



class RedBookSpider(scrapy.Spider):
    name = 'redbooknew'
    start_urls = ['https://www.redbook.com.au/cars/results']

    def parse(self, response):
        
        url = 'https://www.redbook.com.au/cars/results'  # url that requires captcha
        yield Request(url, callback=self.parse_captchad, meta={'solve_captcha': True},
                      errback=self.parse_fail)

    def parse_captchad(self, response):
        solved = response['solved']
        # do stuff

    def parse_fail(self, response):
        pass

    # failed to retrieve captcha in 5 tries :(
    # do stuff

    # def parse(self, response):
    #     print('.....................', response)
        # for products in response.css('a.item'):
        #     print('product  : ', products)
        #     try:
        #         yield {
        #             'price': products.css('div.info span.price::text').get(),
        #             # 'link': products.css().attrib['href'],
        #             # 'image':  products.css('img.product-image-photo').attrib['src']
        #             'desc': products.css('div.desc h3::text').get()
        #         }
        #     except:
        #         yield {
        #             'price': products.css('div.info span.price::text').get(),
        #             # 'link': products.css().attrib['href'],
        #             # 'image':  products.css('img.product-image-photo').attrib['src']
        #             'desc': products.css('div.desc h3::text').get()
        #
        #         }
        #
        # next_page = response.css('li.next a').attrib['href']
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
