import scrapy
from scrapy import Request





class WhiskeySpider(scrapy.Spider):
    name = 'groceries'
    start_urls = ['https://groceries.asda.com/shelf/fresh-food-bakery/party-entertaining/party-cakes-desserts/birthday-party-cakes/1215135760597-1215685031916-1215685801110-1215275467513']

    def parse(self, response):
        for products in response.css('li.co-item'):
            try:
                yield{
                    'name':  products.css('.co-product .co-item__col2 .co-item__title-container h3 a::text').get(),
                     'price':  products.css('.co-product .co-item__col3 .co-item__price-container .co-item__price-per-uom strong').get(),
                     'link': 'https://groceries.asda.com/'+ products.css('.co-product .co-item__col2 .co-item__title-container h3 a').attrib['href'],
                     # 'image':  products.css('img.product-image-photo').attrib['src']
                     # 'ribbon': products.css('div.ribbon-favourite span::text').get()
                }
            except:
               pass




# class groceries(scrapy.Spider):
#     name = 'groceries'
#     start_urls = ['https://groceries.asda.com/shelf/fresh-food-bakery/party-entertaining/party-cakes-desserts/birthday-party-cakes/1215135760597-1215685031916-1215685801110-1215275467513']
#
#     def parse(self, response):
#         for products in response.css('li.co-item'):
#             try:
#                 product_title = products.css('.co-product .co-item__col2 .co-item__title-container h3 a::text').get()
#                 price = products.css('.co-product .co-item__col3 .co-item__price-container .co-item__price-per-uom strong').get()
#                 product_link ='https://groceries.asda.com/'+ products.css('.co-product .co-item__col2 .co-item__title-container h3 a').attrib['href']
#                 yield Request(product_link, self.details_page,
#                               meta={'product_title': product_title, 'product_link': product_link,'price': price})
#             except:
#                 print('Not Working Try Again Later!  ')
#
#     def details_page(self, response):
#         product_title = response.meta['product_title']
#         product_link = response.meta['product_link']
#         price = response.meta['price']
#         for products in response.css('div.product-detail-page__main-detail-cntr'):
#             try:
#                 yield {
#                     'product_title': product_title,
#                     'product_link': product_link,
#                     # 'Product Name': products.css('a.product-item-link::text').get(),
#                     'Price': price,
#                     'Description': products.css('div.pdp-main-details>div>div').get()
#                     # 'image':  products.css('img.product-image-photo').attrib['src']
#                     # 'Date': products.css('div.new-from span::text').get()
#                 }
#             except: pass
#                 #
#                 # yield {
#                 #     'Category': category_name,
#                 #     'Category Link': category_link,
#                 #     'Product Name': products.css('a.product-item-link::text').get(),
#                 #     'Price': products.css('span.price::text').get(),
#                 #     'Link': products.css('a.product-item-link').attrib['href'],
#                 #     # 'image':  products.css('img.product-image-photo').attrib['src']
#                 #     'Date': products.css('div.new-from span::text').get()
#                 # }
#
#         # next_page = response.css('a.action.next').attrib['href']
#         # if next_page is not None:
#         #     yield response.follow(next_page, callback=self.parse)