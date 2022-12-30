import scrapy
from scrapy import Request


class FlipKartSpider(scrapy.Spider):
    name = 'flipkart'
    start_urls = ['https://www.flipkart.com/mobiles-accessories/pr?sid=tyy&otracker=categorytree&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3DMax&sort=popularity']


    # def details_page(self, response):
    #     category_name = response.meta['category_name']
    #     category_link = response.meta['category_link']
    #
    #     for products in response.css('div.product-item-info'):
    #         try:
    #             yield{
    #                 'Category': category_name,
    #                 'Category Link': category_link,
    #                 'Product Name': products.css('a.product-item-link::text').get(),
    #                 'Price': products.css('span.price::text').get(),
    #                 'Link': products.css('a.product-item-link').attrib['href'],
    #                 # 'image':  products.css('img.product-image-photo').attrib['src']
    #                 'Date': products.css('div.new-from span::text').get()
    #             }
    #         except:
    #
    #             yield {
    #                 'Category': category_name,
    #                 'Category Link': category_link,
    #                 'Product Name': products.css('a.product-item-link::text').get(),
    #                 'Price': products.css('span.price::text').get(),
    #                 'Link': products.css('a.product-item-link').attrib['href'],
    #                 # 'image':  products.css('img.product-image-photo').attrib['src']
    #                 'Date': products.css('div.new-from span::text').get()
    #             }
    #
    #     next_page = response.css('a.action.next').attrib['href']
    #     if next_page is not None:
    #         yield response.follow(next_page, callback=self.parse)

    def parse(self, response):

        print(response)
        # for products in response.css('div.d737f398'):
        #         try:
        #             yield{
        #                 'name':  products.css('a').attrib['title'],
        #                  'link': products.css('a').attrib['href'],
        #             }
        #         except:
        #             yield {
        #                 'name':  products.css('a').attrib['title'],
        #                  'link': products.css('a').attrib['href'],
        #             }
        #
        # next_page = response.css('div.b384f4f3 div._1075545d button._31a14546  span._495bfc7d')
        # if next_page is not None:
        #     print('Into the Next Button',next_page)
        #     next_page.click()
        #     yield response.follow(next_page, callback=self.parse)
