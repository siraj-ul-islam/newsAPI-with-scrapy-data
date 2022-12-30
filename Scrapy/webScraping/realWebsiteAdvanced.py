import time

from bs4 import BeautifulSoup
import requests

print("Enter Unfimiler skill :  ")
unfilmer_skill = input('>')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', 'sim-posted').span.text

        if 'few' in published_date:
            campany_job = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfilmer_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name : {campany_job.strip()} \n")
                    f.write(f"skills : {skills.strip()} \n")
                    f.write(f"Published Date: {published_date} \n")
                    f.write(f"More Information: {more_info} \n")
                print(f"File is Saved: {index}")


if __name__ =='__main__':
    while True:
        find_jobs()
        time.sleep(10)