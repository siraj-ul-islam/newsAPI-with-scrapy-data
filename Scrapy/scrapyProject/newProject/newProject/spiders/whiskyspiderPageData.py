import scrapy
from scrapy import Request


# class WhiskeySpider(scrapy.Spider):
#     name = 'newProject'
#     start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']
#
#     def parse(self, response):
#         for products in response.css('div.product-item-info'):
#             try:
#                 yield{
#                     'name':  products.css('a.product-item-link::text').get(),
#                      'price':  products.css('span.price::text').get(),
#                      'link': products.css('a.product-item-link').attrib['href'],
#                      # 'image':  products.css('img.product-image-photo').attrib['src']
#                      'ribbon': products.css('div.ribbon-favourite span::text').get()
#                 }
#             except:
#                 yield {
#                     'name': products.css('a.product-item-link::text').get(),
#                     'price': 'sold out',
#                     'link': products.css('a.product-item-link').attrib['href'],
#                     # 'image':  products.css('img.product-image-photo').attrib['src']
#                     'ribbon': products.css('div.ribbon-favourite span::text').get()
#
#                 }
#
#         next_page = response.css('a.action.next').attrib['href']
#         if next_page is not None:
#             yield response.follow(next_page, callback=self.parse)
#
# class WhiskeySpider(scrapy.Spider):
#     name = 'whiskey'
#     start_urls = ['https://www.whiskyshop.com/']
#
#     def parse(self, response):
#         for products in response.css('li.Level2'):
#             try:
#                 category_name = products.css('a.Level2::text').get()
#                 category_link = products.css('a.Level2').attrib['href']
#                 yield Request(category_link, self.details_page,
#                               meta={'category_name': category_name, 'category_link': category_link})
#             except:
#                 print('Not Working Try Again Later!  ')
#
#     def details_page(self, response):
#         category_name = response.meta['category_name']
#         category_link = response.meta['category_link']
#
#         for products in response.css('div.product-item-info'):
#             try:
#                 yield {
#                     'Category': category_name,
#                     'Category Link': category_link,
#                     'Product Name': products.css('a.product-item-link::text').get(),
#                     'Price': products.css('span.price::text').get(),
#                     'Link': products.css('a.product-item-link').attrib['href'],
#                     # 'image':  products.css('img.product-image-photo').attrib['src']
#                     'Date': products.css('div.new-from span::text').get()
#                 }
#             except:
#
#                 yield {
#                     'Category': category_name,
#                     'Category Link': category_link,
#                     'Product Name': products.css('a.product-item-link::text').get(),
#                     'Price': products.css('span.price::text').get(),
#                     'Link': products.css('a.product-item-link').attrib['href'],
#                     # 'image':  products.css('img.product-image-photo').attrib['src']
#                     'Date': products.css('div.new-from span::text').get()
#                 }
#
#         next_page = response.css('a.action.next').attrib['href']
#         if next_page is not None:
#             yield response.follow(next_page, callback=self.parse)


# product_name = ['New Scotch Whisky', 'New World Whisky', 'New Gin & Spirits', 'View All New Releases ❯',
#                 'Customer Favourites', 'Gift Ideas', 'Flash Sales', 'Award Winning Spirits', 'Peaty Whisky',
#                 'Smoky Whisky', 'Sweet Whisky', 'Floral Whisky', 'Honey Whisky', 'The W Club',
#                 "The Beginner's Guide to Whisky", 'Blog', 'Gift Ideas', 'e-Gift Card', 'Personalised Whisky & Spirits',
#                 'Whisky Gift Sets', 'Whisky Miniatures', 'Whiskies Under £50', 'Whiskies Under £100',
#                 'Whiskies Under £200', 'Wine, Beer & Mixed Drinks', 'View All Whisky Gifts ❯', 'Whisky Glasses',
#                 'Whisky Decanters', 'Whisky Flasks', 'Whisky Books', 'Quaichs', '10 Year Old', '18 Year Old',
#                 '20 Year Old', '21 Year Old', '25 Year Old', '30 Year Old', '40 Year Old', '1992', '1997', '2001',
#                 '2002', '2004', '2012', 'Speyside', 'Islay', 'Highland', 'Lowland', 'Campbeltown', 'Island',
#                 'Single Malt Whisky', 'Single Grain Scotch Whisky', 'Blended Scotch', 'Blended Malts',
#                 'Single Cask Whisky', 'Cask Strength Whisky', 'Sherry Cask Whisky', 'Customer Favourites',
#                 'Limited Editions', 'Rare & Collectable', 'Closed Distilleries', 'Cask Treasures', 'Award Winners',
#                 'Smoky Whisky', 'Peaty Whisky', 'Sweet Whisky', 'Whisky Miniatures', 'Macallan', 'Glenfiddich',
#                 'Dalmore', 'GlenDronach', 'Bowmore', 'Highland Park', 'Benriach', 'Loch Lomond', 'Lagavulin',
#                 'View All Distilleries ❯', 'Johnnie Walker', 'Chivas Regal', 'Compass Box', 'The Loch Fyne',
#                 'Royal Salute', 'View All Brands ❯', 'Japanese Whisky', 'American Whiskey', 'Irish Whiskey',
#                 'Canadian Whisky', 'Taiwanese Whisky', 'Indian Whisky', 'English Whisky', 'Rest of World',
#                 'Customer Favourites', 'Pot Still', 'Rye/Corn', 'Grain Whisky', 'Single Barrel', 'Small Batch',
#                 'Yamazaki', "Blanton's", 'Jack Daniel’s', 'Hibiki', 'Nikka', 'Redbreast', 'Hakushu', 'Woodford Reserve',
#                 'View All Brands ❯', 'Under £50', '£50 - £100', '£100 - £250', 'Over £250', 'Pink Gin', 'Sloe Gin',
#                 'Gin Liqueurs', 'View All ❯', 'Vodka', 'Rum', 'Brandy & Cognac', 'Tequila & Mezcal', 'Other Spirits',
#                 'Cocktail Bundles', 'Premixed Cocktails', 'View All ❯', 'Whisky Liqueurs', 'Gin Liqueurs',
#                 'Cream Liqueurs', 'View All ❯', 'Barware', 'Gin Glasses', 'Gin Miniatures']
#
# links = ['https://www.whiskyshop.com/newreleases/new-scotch-whisky',
#          'https://www.whiskyshop.com/newreleases/new-world-whisky',
#          'https://www.whiskyshop.com/newreleases/new-gin-spirits', 'https://www.whiskyshop.com/newreleases',
#          'https://www.whiskyshop.com/scotch-whisky/customer-favourites', 'https://www.whiskyshop.com/gift-ideas',
#          'https://www.whiskyshop.com/offers/flash-sales', 'https://www.whiskyshop.com/award-winners',
#          'https://www.whiskyshop.com/flavour/peaty-whisky', 'https://www.whiskyshop.com/flavour/smoky-whisky',
#          'https://www.whiskyshop.com/flavour/sweet-whisky', 'https://www.whiskyshop.com/flavour/floral-whisky',
#          'https://www.whiskyshop.com/flavour/honey-whisky', 'https://www.whiskyshop.com/club',
#          'https://www.whiskyshop.com/beginners-guide', 'https://www.whiskyshop.com/blog',
#          'https://www.whiskyshop.com/gift-ideas', 'https://www.whiskyshop.com/e-gift-card',
#          'https://www.whiskyshop.com/personalised-whisky-engraving', 'https://www.whiskyshop.com/gifts/gift-sets',
#          'https://www.whiskyshop.com/gifts/whisky-miniatures', 'https://www.whiskyshop.com/gifts/whiskies-under-50',
#          'https://www.whiskyshop.com/gifts/whiskies-under-100', 'https://www.whiskyshop.com/gifts/whiskies-under-200',
#          'https://www.whiskyshop.com/gifts/wine-beer', 'https://www.whiskyshop.com/gifts',
#          'https://www.whiskyshop.com/gifts/whisky-glasses', 'https://www.whiskyshop.com/gifts/whisky-decanters',
#          'https://www.whiskyshop.com/gifts/whisky-flasks', 'https://www.whiskyshop.com/gifts/whisky-books',
#          'https://www.whiskyshop.com/gifts/quaichs', 'https://www.whiskyshop.com/gifts/10-year-old-whisky',
#          'https://www.whiskyshop.com/gifts/18-year-old-whisky', 'https://www.whiskyshop.com/gifts/20-year-old-whisky',
#          'https://www.whiskyshop.com/gifts/21-year-old-whisky', 'https://www.whiskyshop.com/gifts/25-year-old-whisky',
#          'https://www.whiskyshop.com/gifts/30-year-old-whisky', 'https://www.whiskyshop.com/gifts/40-year-old-whisky',
#          'https://www.whiskyshop.com/scotch-whisky/all?vintage=1992',
#          'https://www.whiskyshop.com/scotch-whisky/all?vintage=1997',
#          'https://www.whiskyshop.com/scotch-whisky/all?vintage=2001',
#          'https://www.whiskyshop.com/scotch-whisky/all?vintage=2002',
#          'https://www.whiskyshop.com/scotch-whisky/all?vintage=2004',
#          'https://www.whiskyshop.com/scotch-whisky/all?vintage=2012',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/speyside',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/islay',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/highland',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/lowland',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/campbeltown',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/island',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky',
#          'https://www.whiskyshop.com/single-grain-scotch-whisky', 'https://www.whiskyshop.com/blended-scotch-whisky',
#          'https://www.whiskyshop.com/blended-malts',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/single-cask-whisky',
#          'https://www.whiskyshop.com/cask-strength-whisky', 'https://www.whiskyshop.com/sherry-cask-whisky',
#          'https://www.whiskyshop.com/scotch-whisky/customer-favourites', 'https://www.whiskyshop.com/limited-editions',
#          'https://www.whiskyshop.com/scotch-whisky/rare-collectable-whiskies',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/closed-distilleries',
#          'https://www.whiskyshop.com/scotch-whisky/cask-treasures',
#          'https://www.whiskyshop.com/award-winners?classification=Scotch+Whisky',
#          'https://www.whiskyshop.com/flavour/smoky-whisky', 'https://www.whiskyshop.com/flavour/peaty-whisky',
#          'https://www.whiskyshop.com/flavour/sweet-whisky', 'https://www.whiskyshop.com/gifts/whisky-miniatures',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/distilleries/macallan',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/distilleries/glenfiddich',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/distilleries/dalmore',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/distilleries/glendronach',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/distilleries/bowmore',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/distilleries/highland-park',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/distilleries/benriach',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/distilleries/loch-lomond',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/distilleries/lagavulin',
#          'https://www.whiskyshop.com/single-malt-scotch-whisky/distilleries',
#          'https://www.whiskyshop.com/blended-scotch-whisky/brand/johnnie-walker',
#          'https://www.whiskyshop.com/blended-scotch-whisky/brand/chivas-regal',
#          'https://www.whiskyshop.com/blended-scotch-whisky/brand/compass-box',
#          'https://www.whiskyshop.com/blended-scotch-whisky/brand/the-loch-fyne',
#          'https://www.whiskyshop.com/blended-scotch-whisky/brand/royal-salute',
#          'https://www.whiskyshop.com/blended-scotch-whisky/brand',
#          'https://www.whiskyshop.com/world-whiskies/japanese-whisky',
#          'https://www.whiskyshop.com/world-whiskies/american-whiskey',
#          'https://www.whiskyshop.com/world-whiskies/irish-whiskey',
#          'https://www.whiskyshop.com/world-whiskies/canadian-whisky',
#          'https://www.whiskyshop.com/world-whiskies/taiwanese-whisky',
#          'https://www.whiskyshop.com/world-whiskies/indian-whisky',
#          'https://www.whiskyshop.com/world-whiskies/english-whisky',
#          'https://www.whiskyshop.com/world-whiskies/rest-of-world',
#          'https://www.whiskyshop.com/world-whiskies/favourites', 'https://www.whiskyshop.com/world-whiskies/pot-still',
#          'https://www.whiskyshop.com/world-whiskies/rye-corn', 'https://www.whiskyshop.com/world-whiskies/grain',
#          'https://www.whiskyshop.com/world-whiskies/single-barrel',
#          'https://www.whiskyshop.com/world-whiskies/small-batch',
#          'https://www.whiskyshop.com/world-whiskies/brand/yamazaki',
#          'https://www.whiskyshop.com/world-whiskies/brand/blantons',
#          'https://www.whiskyshop.com/world-whiskies/brand/jack-daniels',
#          'https://www.whiskyshop.com/world-whiskies/brand/hibiki',
#          'https://www.whiskyshop.com/world-whiskies/brand/nikka',
#          'https://www.whiskyshop.com/world-whiskies/brand/redbreast',
#          'https://www.whiskyshop.com/world-whiskies/brand/hakushu',
#          'https://www.whiskyshop.com/world-whiskies/brand/woodford-reserve',
#          'https://www.whiskyshop.com/world-whiskies/brand', 'https://www.whiskyshop.com/world-whiskies?price=-50',
#          'https://www.whiskyshop.com/world-whiskies?price=50-100',
#          'https://www.whiskyshop.com/world-whiskies?price=100-250',
#          'https://www.whiskyshop.com/world-whiskies?price=250-', 'https://www.whiskyshop.com/gin/pink-gin',
#          'https://www.whiskyshop.com/gin/sloe-gin', 'https://www.whiskyshop.com/gin/gin-liqueurs',
#          'https://www.whiskyshop.com/gin', 'https://www.whiskyshop.com/vodka', 'https://www.whiskyshop.com/rum',
#          'https://www.whiskyshop.com/brandy-cognac', 'https://www.whiskyshop.com/tequila-mezcal',
#          'https://www.whiskyshop.com/other-spirits', 'https://www.whiskyshop.com/cocktails/bundles',
#          'https://www.whiskyshop.com/cocktails/premixed', 'https://www.whiskyshop.com/spirits',
#          'https://www.whiskyshop.com/liqueurs/whisky-liqueurs', 'https://www.whiskyshop.com/gin/gin-liqueurs',
#          'https://www.whiskyshop.com/liqueurs/cream-liqueurs', 'https://www.whiskyshop.com/liqueurs',
#          'https://www.whiskyshop.com/gifts/barware', 'https://www.whiskyshop.com/gin/gin-glasses',
#          'https://www.whiskyshop.com/gin/gin-miniatures']


#
class WhiskeySpider(scrapy.Spider):
    name = 'Project'
    start_urls = ['https://www.instagram.com/atlfoodiesofficial/followers/']

    def parse(self, response):
        for products in response.css('div._abcm'):
            try:
                yield{
                    'Distillery/Brand': products.css('a::href').get(),
                    # 'Region': products.css('dd a::text').get(),
                    # 'Style': products.css('dd a::text').get(),
                    # 'Distillery/Brand': products.css('dd a::text').get(),
                }
            except:
                yield {
                    # 'Distillery/Brand': products.css('dd a::text').get(),
                    # 'Region': products.css('dd a::text').get(),
                    # 'Style': products.css('dd a::text').get(),
                }

        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
