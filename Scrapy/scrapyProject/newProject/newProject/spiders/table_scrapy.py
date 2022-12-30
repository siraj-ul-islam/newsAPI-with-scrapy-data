import scrapy
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



# def ImplicitWait(self):
#         driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
#         driver.implicitly_wait(10)
#         driver.get("https://www.montmere.com/test.php")
#         driver.maximize_window()
#         driver.find_element(By.ID, "username").send_keys("Siraj ul islam")
#         driver.find_element(By.ID, "password").send_keys("Siraj ul islam")
#         driver.find_element(By.XPATH, "//input[@value='Login']").click()


# not working fine

class blog_Post(scrapy.Spider):
    name = 'test'
    start_urls = ['https://www.montmere.com/test.php']

    def __init__(self):
        driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        driver.implicitly_wait(10)
        driver.get("https://www.montmere.com/test.php")
        driver.maximize_window()
        driver.find_element(By.ID, "username").send_keys("Siraj ul islam")
        driver.find_element(By.ID, "password").send_keys("Siraj ul islam")
        driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(5)


    def parse(self, response):
        self.driver.get('https://www.montmere.com/test.php')
        for post in response.css('table.table'):
            try:
                # auth_name = post.css('.oxy-post-wrap div.oxy-post-meta div.oxy-post-meta-author::text')[0].get()
                # auth_name = self.strip_tabes_and_newlines(auth_name)
                # image_url = post.css('.oxy-post-wrap a::attr(href)').get()
                # image_url = add_domain_name_with_url(image_url)
                yield {
                    'text':  post.css('tr').get()

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







