from django.shortcuts import render
from .models import NewsModel
import requests
import json
import os
from dotenv import load_dotenv 
import sqlite3

load_dotenv()

def API_data(search_query=None):
    try:
        

        querystring = {"q":search_query,"pageNumber":"1","pageSize":"10","autoCorrect":"true","fromPublishedDate":"null","toPublishedDate":"null"}

        headers = {
            'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
            'x-rapidapi-key': os.environ.get("api_key")
        }

        if search_query:
            url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/NewsSearchAPI"
            
            response = requests.request("GET", url, headers=headers, params=querystring)
        else:
            url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/TrendingNewsAPI?pageNumber=1&pageSize=10&withThumbnails=false&location=IN"

            response = requests.request("GET", url, headers=headers)

        response_data=json.loads(response.text)

        return response_data["value"]
    
    except BaseException as e:
        print(e)

def Home(request):
    
    company=request.POST.get('id_type')

    if company:
        news_list=NewsModel.objects.filter(dictionary_tokens=company)
    else:
        news_list=NewsModel.objects.all()

    
    return render(request,'home.html',context={'news_list':news_list})

def all_news(request):
    
    query=request.GET.get('search_query')

    response_data=API_data(query)

    return render(request,'all_news.html',context={'articles':response_data})