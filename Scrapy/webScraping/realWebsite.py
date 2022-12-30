from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date = job.find('span', 'sim-posted').span.text

    if 'few' in published_date:
        campany_job = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        # print(campany_job)
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        # print(skills)
        # print(published_date)




        print(f'''
        Company Name : {campany_job}
        skills : {skills}
        Published Date: {published_date}
        ''')
        print('............................................')