from ast import For
from django.shortcuts import render

import requests
# Create your views here.


def index(request):
    url ="https://newsapi.org/v2/top-headlines?country=us&apiKey=8d3d8b7c0ecc4aceaa1b483bf1027031"

    response = requests.get(url).json()

    a = response['articles']
    t = response['totalResults']

    print(t)
    
    desc = []
    title = []
    img= []

    for i in range(len(a)):
        print(i)
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(title, desc, img, )
    context = {'mylist':mylist}

    return render(request, 'index.html', context)
