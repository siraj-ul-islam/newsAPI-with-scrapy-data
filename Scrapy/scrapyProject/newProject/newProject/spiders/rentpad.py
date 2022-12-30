import datetime
import time

import scrapy
import re


class RentpadSpider(scrapy.Spider):

    name = "rented"
    # start_urls = ['https://rentpad.com.ph/listing/a8112f6957&cl=1&fl=1']

    # Apartment & Condo
    start_urls = ['https://rentpad.com.ph/long-term-rentals/cebu/fully-furnished-1-bedroom-unit-at-mivesa-garden-residences/90135b0f90&cl=1',
        'https://rentpad.com.ph/long-term-rentals/cebu/great-location-space-at-grand-residences-cebu-city/d516dcb79&cl=1',
        'https://rentpad.com.ph/long-term-rentals/davao/fully-furnished-studio-unit-at-arezzo-place-davao-for-rent/d93d08fd45&cl=1']

    def remove_white_space_and_extra_things(self, data):
        if data:
            data = data.strip()
            data = data.replace(">>", " ").strip()
            data = data.replace("\r\n", " ").strip()
            data = data.replace("\r", " ").strip()
            data = data.replace("\n\n", " ").strip()
            data = data.replace("\n", " ").strip()
            data = data.strip()

        return data

    def parse(self, response):
        # for products in response.css('div.view-tile-left-floater.listing-holder'):
        price = response.xpath('//span[@itemprop="price"]/text()').get()
        price = price[1:]
        Bedrooms = self.remove_white_space_and_extra_things(response.xpath('//table[@id="table-listing-details"]//td[contains(text(),"Bedrooms")]/following-sibling::td/text()').get())
        Bathrooms = self.remove_white_space_and_extra_things(response.xpath('//table[@id="table-listing-details"]//td[contains(text(),"Bathrooms")]/following-sibling::td/text()').get())
        city = self.remove_white_space_and_extra_things(response.xpath('//table[@id="table-listing-details"]//td[contains(text(),"City")]/following-sibling::td/a/text()').get())
        Area = self.remove_white_space_and_extra_things(response.xpath('//table[@id="table-listing-details"]//td[contains(text(),"Square Area")]/following-sibling::td/text()').get())
        Square_Area = Area[:-3]
        Area_Unit = Area[-3:]
        # description = self.remove_white_space_and_extra_things(response.xpath('//table//td//b[contains(text(),"Description")]/following-sibling::span/text()|//table//td//b[contains(text(),"Description")]/following-sibling::span/div/text()|//table//td//b[contains(text(),"Description")]/following-sibling::span/div/div/text()').getall())
        description = self.remove_white_space_and_extra_things(response.xpath('normalize-space(//table//td//b[contains(text(),"Description")]/following-sibling::span)').get())
        first_50_discription = description[:200]
        print("first_50_discription........", first_50_discription)
        listing_id = re.findall('[^\/]+(?=\=[^\/.]*$)', response.url)
        listing_id = listing_id[0]

        agency_name = self.remove_white_space_and_extra_things(response.xpath('//div[@id="contact-name"]/text()').get())
        current_date = datetime.datetime.now()
        current_date = current_date.strftime("%D")
        listing_on = self.remove_white_space_and_extra_things(response.xpath('//table[@id="table-listing-details"]//td[contains(text(),"Updated")]/following-sibling::td/text()').get())

        yield {
            'Site': 'Rentpad',
            'Offer Type': 'Rental',
            'URL': response.url,
            'Title': response.xpath('//span[@itemprop="name"]/text()').get(),
            'Property Type': 'Apartment & Condo',
            'Price': price,
            'Bedrooms': Bedrooms,
            'Bathrooms': Bathrooms,
            'Area Size': Square_Area,
            'Area Unit': Area_Unit,
            'Address': response.xpath('//span[@style= "font-size:14px; font-weight: normal; margin-top:10px; position: relative; top:-5px;"]/text()').get(),
            'Location': city,
            'First 50 letters of the description': first_50_discription,
            'Alternate Property Type (applicable in some cases)': ' ',
            'Listing ID': listing_id,
            'Listed On (If available)': listing_on,
            'Agent Name': ' ',
            'Agency Name': agency_name,
            'Agency Phone': ' ',
            'Agency Url': response.xpath('//div[@id="contact-name"]/parent::a/@href').get(),
            'Agency Email': ' ',
            'Date Scrapped': current_date,

        }



        # next_page = response.xpath("//input[@id='btn-page-next']").attrib('onclick')










