#
#
# url = "http://www.google.com.pk/search?q"
# # url = "http://www.google.com/search?q"
#
# value1 = url.split('/search')
#
# print (value1)
# v = value1[0]
#
# value2 =value1[0].split('.com')
#
# print (value2)
#
# if 'google.com'+value2[1]+'/search' in url:
#     print ('value is present')
# else:
#     print('try agian later')
#
# value3 =  'google.com'+value2[1]+'/search'
# print (value3)

import csv
import pandas as pd


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
#
#
# def strip_tabes_and_newlines(rows):
#     correct_name = []
#     for name in rows:
#         # name = "\n\t\t\tBy Neha Setia Nagpal\t\t"
#         first_strip_tabes = name.strip('\t')
#         newline_strip = first_strip_tabes.strip('\n')
#         second_strip_tabes = newline_strip.strip('\t')
#         full_name = second_strip_tabes
#         correct_name.append(full_name)
#         print("Name is ", full_name, "Good day")
#     print(correct_name)
#
#
# strip_tabes_and_newlines(rows)
#
#
# def add_domain_name_with_url(urls):
#     # url = "/blog/why-are-rotating-proxies-important/"
#     total_urls = []
#     domain_name = "https://www.zyte.com"
#     for url in urls:
#         full_url = domain_name + url
#         total_urls.append(url)
#
#         print("Full url is : ", full_url)
#     print(total_urls)
#
#
# add_domain_name_with_url(url)


def store_updated_data_in_csv_file():

    # reading the csv file
    df = pd.read_csv("blogpost.csv")

    # updating the column value/data
    df['author'] = df['author'].replace({'': 'Blog'})

    # writing into the file
    df.to_csv("blogpost.csv", index=False)

    print(df)

store_updated_data_in_csv_file()