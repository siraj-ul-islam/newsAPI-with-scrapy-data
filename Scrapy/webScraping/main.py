from bs4 import BeautifulSoup

with open('home.html',  encoding="utf8")as html_file:
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    # title = soup.find('title')
    # print(title.text)
    # a_tags = soup.find_all('a')
    # for a in a_tags:
    #     print(a.text)
    quotes = soup.find_all('div',class_="quote")
    for q in quotes:
        # print(q)
        # print(q.a)
        a_text = q.div.a.text.split()[-1]
        span_text = q.span.small
        print(a_text)
        print(span_text)
        print(f'{a_text} span_text is {span_text}')