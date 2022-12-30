import scrapy


class inmuebles24(scrapy.Spider):
    name = 'inmuebles24'
    start_urls = ['https://www.inmuebles24.com/departamentos-en-temporal-vacacional.html']

    def parse(self, response):
        for products in response.css('div.postingCardContent'):
            try:
                yield{
                    'image':  products.css('div.slide-content img::src').get(),
                     'price':  products.css('div.postingCardPrices span.firstPrice::text').get(),
                     # 'link': products.css('a.product-item-link').attrib['href'],
                     # # 'image':  products.css('img.product-image-photo').attrib['src']
                     # 'ribbon': products.css('div.ribbon-favourite span::text').get()
                }
            except:
                yield {
                    # 'name': products.css('a.product-item-link::text').get(),
                    # 'price': 'sold out',
                    # 'link': products.css('a.product-item-link').attrib['href'],
                    # # 'image':  products.css('img.product-image-photo').attrib['src']
                    # 'ribbon': products.css('div.ribbon-favourite span::text').get()

                }
        # next_page = response.css('a.action.next').attrib['href']
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
