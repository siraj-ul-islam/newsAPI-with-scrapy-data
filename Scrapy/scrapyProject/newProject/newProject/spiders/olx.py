import json

import scrapy
from scrapy import Request
import requests


class OlxSpider(scrapy.Spider):
    name = 'olxnew'
    all_urls = []
    for x in range(2):

        url = 'https://www.olx.com.pk/?page={index}'.format(index=x)
        # url = 'https://www.olx.com.pk/mobile-phones_c1453?page={index}'.format(index=x)

        if url not in all_urls:
            all_urls.append(url)

    start_urls = all_urls

    def parse(self, response):
        if response.css('div.d737f398'):
            for products in response.css('div.d737f398'):
                try:
                    name = products.css('a').attrib['title']
                    link = 'https://www.olx.com.pk' + products.css('a').attrib['href']
                    price = products.css('div._41d2b9f3 div._88d4ee64 span::text').get()
                    location = products.css('div._5ea5614c div.afabcb7f span._424bf2a8::text').get()
                    week_a_go_Post = products.css('div._5ea5614c div.afabcb7f span._2e28a695 span::text').get()
                    KM_drive = 'None'
                    yield Request(link, self.details_page,
                                  meta={'name': name, 'link': link, 'KM_drive': KM_drive, 'price': price,
                                        'location': location, 'week_a_go_Post': week_a_go_Post})

                except:
                    name = products.css('a').attrib['title']
                    link = 'https://www.olx.com.pk' + products.css('a').attrib['href']
                    price = products.css('div._41d2b9f3 div._88d4ee64 span::text').get()
                    location = products.css('div._5ea5614c div.afabcb7f span._424bf2a8::text').get()
                    week_a_go_Post = products.css('div._5ea5614c div.afabcb7f span._2e28a695 span::text').get()
                    KM_drive = 'None'
                    yield Request(link, self.details_page,
                                  meta={'name': name, 'link': link, 'KM_drive': KM_drive, 'price': price,
                                        'location': location, 'week_a_go_Post': week_a_go_Post})

        elif response.css('div.a52608cc'):

            for products in response.css('div.a52608cc'):
                try:
                    name = products.css('a').attrib['title']
                    link = 'https://www.olx.com.pk' + products.css('a').attrib['href']
                    KM_drive = products.css('div._4dbba078 div.a8f6df88 span.fef55ec1 span::text').get()
                    # Car_Modal =  products.css('div._4dbba078 div.a8f6df88 span.fef55ec1 span.c47715cd::text').get()
                    price = products.css('div._41d2b9f3 div._52497c97 span::text').get()
                    location = products.css('div._2fc90438 span._424bf2a8::text').get()
                    week_a_go_Post = products.css('div._2fc90438 span._2e28a695 span::text').get()
                    yield Request(link, self.details_page,
                                  meta={'name': name, 'link': link, 'KM_drive': KM_drive, 'price': price,
                                        'location': location, 'week_a_go_Post': week_a_go_Post})


                except:
                    name = products.css('a').attrib['title']
                    link = 'https://www.olx.com.pk' + products.css('a').attrib['href']
                    KM_drive = products.css('div._4dbba078 div.a8f6df88 span.fef55ec1 span::text').get()
                    # Car_Modal = products.css('div._4dbba078 div.a8f6df88 span.fef55ec1 span.c47715cd::text').get()
                    price = products.css('div._41d2b9f3 div._52497c97 span::text').get()
                    location = products.css('div._2fc90438 span._424bf2a8::text').get()
                    week_a_go_Post = products.css('div._2fc90438 span._2e28a695 span::text').get()
                    yield Request(link, self.details_page,
                                  meta={'name': name, 'link': link, 'KM_drive': KM_drive, 'price': price,
                                        'location': location, 'week_a_go_Post': week_a_go_Post})

    def details_page(self, response):
        name = response.meta['name']
        link = response.meta['link']
        price_main_page = response.meta['price']
        location = response.meta['location']
        week_a_go_Post = response.meta['week_a_go_Post']
        km_used = response.meta['KM_drive']

        price = response.xpath(
            "(//div[@class='cf4781f0'] //div[@class='_59317dec'] //div[@class='_241b3b1e'] //div[@class='_676a547f']//div[@class='b44ca0b3']//span)[2]/text()").get()
        year = response.xpath(
            "(//div[@class='cf4781f0'] //div[@class='_59317dec'] //div[@class='_241b3b1e'] //div[@class='_676a547f']//div[@class='b44ca0b3']//span)[8]/text()").get()
        make = response.xpath(
            "(//div[@class='cf4781f0'] //div[@class='_59317dec'] //div[@class='_241b3b1e'] //div[@class='_676a547f']//div[@class='b44ca0b3']//span)[4]/text()").get()
        condition = response.xpath(
            "(//div[@class='cf4781f0'] //div[@class='_59317dec'] //div[@class='_241b3b1e'] //div[@class='_676a547f']//div[@class='b44ca0b3']//span)[6]/text()").get()

        for products in response.css('div.cf4781f0'):

            phone = self.get_phone_number(link)
            print(phone)
            try:
                yield {
                    'Name': name,
                    'Link': link,
                    'Price Main Page': price_main_page,
                    'Location': location,
                    'KM Used': km_used,
                    'week_a_go_Post': week_a_go_Post,
                    'Phone Number': phone,
                    'Description': products.css('div._59317dec div._0f86855a span::text').get(),
                    'Price': price,
                    'Year': year,
                    'Make': make,
                    'Car Condition': condition,

                }
            except:
                yield {
                    'Name': name,
                    'Link': link,
                    'Price': price,
                    'Location': location,
                    'KM Used': km_used,
                    'week_a_go_Post': week_a_go_Post,
                    'Phone Number': phone,
                    'Description': products.css('div._59317dec div._0f86855a span::text').get(),
                    'Price Main Page': 'None',
                    'Year': 'None',
                    'Make': 'None',
                    'Condition': 'None'

                }

    def get_phone_number(self, link):

        url_id = self.split_string_url(link)

        url = 'https://www.olx.com.pk/api/users/search/?adExternalIDs='+url_id+'&format=lite'

        cookies_string = 'device_id=l168piq9n3q5oonuj; _gcl_au=1.1.899016548.1648201656; _fbp=fb.2.1648201657205.1723528898; __gads=ID=11ab2be9c2489d4a:T=1648201657:S=ALNI_MZ0ScMMnoPfDujBBm_4cpg5ds6jlQ; __gpi=UID=000003a44d2bc9b9:T=1649314732:RT=1649314732:S=ALNI_MaGzzWQADHPQNvK8zmq_tJyBQB12g; g_state={"i_p":1650005482960,"i_l":3}; settings=%7B%22area%22%3Anull%2C%22currency%22%3A%22PKR%22%2C%22installBanner%22%3Atrue%2C%22searchHitsLayout%22%3A%22LIST%22%7D; abTests=%7B%7D; banners=%7B%7D; userGeoLocation=%7B%22coordinates%22%3Anull%2C%22closestLocation%22%3Anull%2C%22error%22%3Anull%2C%22loading%22%3Afalse%7D; _gid=GA1.3.1078052196.1649654790; OPT_IN_SHOWN_TIME=1649654798401; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; USER_DATA=%7B%22attributes%22%3A%5B%7B%22key%22%3A%22USER_ATTRIBUTE_UNIQUE_ID%22%2C%22value%22%3A%2210900089-d397-47d1-9e93-39c2c6e382c6%22%7D%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%22e4b6f364-ee07-46c9-b5d7-0cbe80233eba%22%2C%22deviceAdded%22%3Atrue%7D; anonymous_session_id=26c92873-8384-4677-9ee7-bd3f5919269c; moe_uuid=e4b6f364-ee07-46c9-b5d7-0cbe80233eba; kc_access_token=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTNG1Dd1NGbGR0SmEyMjFVampGM2NyeVg5bThhOFcyVlpBR2poS3B4WlNzIn0.eyJleHAiOjE2NDk3Mzk5MjUsImlhdCI6MTY0OTczOTAyNSwiYXV0aF90aW1lIjoxNjQ5NjU2NDc0LCJqdGkiOiI0OWFhNzA4OC1jNmRjLTQwOGEtYjNiNC1mMjk3N2FlZjEyODYiLCJpc3MiOiJodHRwczovL2F1dGgub2x4LmNvbS5way9hdXRoL3JlYWxtcy9vbHgtcGsiLCJzdWIiOiIxMDkwMDA4OS1kMzk3LTQ3ZDEtOWU5My0zOWMyYzZlMzgyYzYiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJmcm9udGVuZCIsInNlc3Npb25fc3RhdGUiOiI5YTc4OTIyNi0zYjJmLTQ5MGQtOTdmOC00NDIxNTJmZDQ2ZjQiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHBzOi8vd3d3Lm9seC5jb20ucGsiLCJvbHgtcGs6LyIsImh0dHBzOi8vb2x4LmNvbS5wayIsImh0dHBzOi8vc3RyYXQub2x4LmNvbS5wayJdLCJzY29wZSI6Im9wZW5pZCB1c2VyX3Byb2ZpbGUiLCJleHRlcm5hbF9pZCI6IjEwOTAwMDg5LWQzOTctNDdkMS05ZTkzLTM5YzJjNmUzODJjNiJ9.XMwuML6D5jnynhncbeiRzXmE42Qx6q8wjIoBOb8uSh5qh35uHnVQp3o7mI1uKTUlSoDwH9S12IBZeb8K82TM5X7kOPmW4vt-kAurPAiVvplOOFy7PjrRZqbdcFUiTm40eLSTCscXfxm953zN5F_HMpon2CYZqACQj-SEySzuaORgliLoz860krYXsDLLkcYMgFbc6H9ECgmYmKvBmoy1B4syxCy0dmQdwVsmklZF8JlVR1hpjLougyvNIWa2Kl4AWpWoDp9_1XEeqeccy_brGfIwv8fQ66uMKgXPboidLspCNJS2JVXJMLocPci_2b9zS_yy1g6CoCKPAqEqd0yaww; kc_refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJlNGU1MjI1MS05M2U0LTQwYTItYjQ3Yy01NTBkYWY5ODZhN2EifQ.eyJleHAiOjE2NTIzMzEwMjUsImlhdCI6MTY0OTczOTAyNSwianRpIjoiOTE3ODdhMWYtZjQ5ZC00Y2FiLTk3N2EtMTE5NjZmNzU3ZmM2IiwiaXNzIjoiaHR0cHM6Ly9hdXRoLm9seC5jb20ucGsvYXV0aC9yZWFsbXMvb2x4LXBrIiwiYXVkIjoiaHR0cHM6Ly9hdXRoLm9seC5jb20ucGsvYXV0aC9yZWFsbXMvb2x4LXBrIiwic3ViIjoiMTA5MDAwODktZDM5Ny00N2QxLTllOTMtMzljMmM2ZTM4MmM2IiwidHlwIjoiUmVmcmVzaCIsImF6cCI6ImZyb250ZW5kIiwic2Vzc2lvbl9zdGF0ZSI6IjlhNzg5MjI2LTNiMmYtNDkwZC05N2Y4LTQ0MjE1MmZkNDZmNCIsInNjb3BlIjoib3BlbmlkIHVzZXJfcHJvZmlsZSJ9.a_hf4rpGbgJD0P05itBblEwi64fZD_XEQU0FQXbnybk; kc_id_token=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTNG1Dd1NGbGR0SmEyMjFVampGM2NyeVg5bThhOFcyVlpBR2poS3B4WlNzIn0.eyJleHAiOjE2NDk3Mzk5MjUsImlhdCI6MTY0OTczOTAyNSwiYXV0aF90aW1lIjoxNjQ5NjU2NDc0LCJqdGkiOiJkNDQyOWY1ZS1iOWE4LTRmNzMtOTcyNy1mY2FjODU0NWY1YTIiLCJpc3MiOiJodHRwczovL2F1dGgub2x4LmNvbS5way9hdXRoL3JlYWxtcy9vbHgtcGsiLCJhdWQiOiJmcm9udGVuZCIsInN1YiI6IjEwOTAwMDg5LWQzOTctNDdkMS05ZTkzLTM5YzJjNmUzODJjNiIsInR5cCI6IklEIiwiYXpwIjoiZnJvbnRlbmQiLCJzZXNzaW9uX3N0YXRlIjoiOWE3ODkyMjYtM2IyZi00OTBkLTk3ZjgtNDQyMTUyZmQ0NmY0IiwiYWNyIjoiMSIsImlkZW50aXR5X3Byb3ZpZGVycyI6WyJnb29nbGUiXSwibmFtZSI6IlNpcmFqIFVsIElzbGFtIiwiZXh0ZXJuYWxfaWQiOiIxMDkwMDA4OS1kMzk3LTQ3ZDEtOWU5My0zOWMyYzZlMzgyYzYiLCJlbWFpbCI6InNpcmFqQGFpdG9tYXRpb24uY29tIiwiaXNfcGFzc3dvcmRsZXNzX2xvZ2luIjp0cnVlfQ.UzvKFxzfli5f6z9In1hk4F1Tnlx13-bsr3EopKwWK9UqKV7r-lC9S6cVubZE7elLq_pFJg70ZwQDd8IiBi1ToFc1n2vzBYdwSRSp9sNkWBI4FNPJM2U4z3tlegZ5ouBGffqGyOK6dhm9VoWXBlOUHKNOhk8LPgh2xuI6dQfYyU5ZrS9VyhMePwOdqDH04dx8u2cXJILdbre5KWgrP6dUZ2GM4aMOyRFgokVKUmzlSCiIho6k2QfdYjyNEAg0EqrxpOS0LdW3qrlFyWNlnT5MeuubnX-n0JnYBGKxbdxsJ4xMMd9F-ZiH0FSBFz5QYjO3VpzpDB03_CNBBfnAPM9zVA; _ga=GA1.3.1463106906.1648201657; _gat_UA-192624154-2=1; _ga_YP1ZBNYRVD=GS1.1.1649737905.14.1.1649739208.60; referrer=%2F%3Fpage%3D1; landing_url=%2F'
        headers = {
            'accept': 'application/json',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en',
            'cookie': cookies_string,
            'referer' : link,
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Windows',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',

        }
        result = requests.get(url, headers=headers)

        data = json.loads(result.text)

        phone_number =  data[0]['phoneNumber']

        return phone_number

    def split_string_url(self, get_url):
        string_value = get_url.split("iid-")
        get_url = string_value[1]
        print("Get First string  value: ", get_url)
        return get_url
