import scrapy

# not working fine

class blog_Post(scrapy.Spider):
    name = 'olx'
    start_urls = ['https://www.olx.com.pk/cars_c84']

    def strip_tabes_and_newlines(self, name):
        correct_name = []
        # for name in rows:
        # name = "\n\t\t\tBy Neha Setia Nagpal\t\t"
        first_strip_tabes = name.strip('\t')
        newline_strip = first_strip_tabes.strip('\n')
        second_strip_tabes = newline_strip.strip('\t')
        full_name = second_strip_tabes
        correct_name.append(full_name)
        print("Name is ", full_name, "Good day")
        return full_name
        # print(correct_name)

    def parse(self, response):
        for post in response.css('div._1075545d'):
            try:
                # auth_name = post.css('.oxy-post-wrap div.oxy-post-meta div.oxy-post-meta-author::text')[0].get()
                # auth_name = self.strip_tabes_and_newlines(auth_name)
                # image_url = post.css('.oxy-post-wrap a::attr(href)').get()
                # image_url = add_domain_name_with_url(image_url)
                yield {
                    'text':  post.css('ul li').get()

                    # 'href': post.css('div.ec').get(),
                    # 'href': post.css('.b3onmgus.sonix8o1 div.a8c37x1j div.kbiprv82 a::attr(href)').get(),
                    # 'image_url': image_url,
                    # 'title': post.css('.oxy-post-wrap div a::text')[0].get(),
                    # 'author': auth_name,
                }

            except:
                # auth_name = post.css('.oxy-post-wrap div.oxy-post-meta div.oxy-post-meta-author::text')[0].get()
                # auth_name = self.strip_tabes_and_newlines(auth_name)
                # image_url = post.css('.oxy-post-wrap a::attr(href)').get()
                # image_url = add_domain_name_with_url(image_url)
                yield {
                    # 'href': post.css('div div div span div  div a::attr(href)').get(),
                    # 'image_url': image_url,
                    # 'title': post.css('.oxy-post-wrap div a::text')[0].get(),
                    # 'author': auth_name,
                }
        # next_page = response.css('button.bs').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)


def add_domain_name_with_url(url):
    # url = "/blog/why-are-rotating-proxies-important/"
    total_urls = []
    domain_name = "https://www.zyte.com"
    # for url in urls:
    full_url = domain_name + url
    total_urls.append(url)

    print("Full url is : ", full_url)
    return full_url
    print(total_urls)





# import csv
#
# rows = []
# url = []
# with open("blogpost.csv", 'r', encoding="utf8") as file:
#     csvreader = csv.reader(file)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row[3] + '')
#         url.append(row[1] + '')
# print(header)
# print(rows)
# print(url)
