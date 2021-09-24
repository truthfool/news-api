from django.shortcuts import render
from .models import NewsModel
import requests
import json
import os
from dotenv import load_dotenv 

load_dotenv()
# Create your views here.
def API_data():
    try:
        url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/TrendingNewsAPI?pageNumber=1&pageSize=10&withThumbnails=false&location=IN"

        payload={}
        headers = {
            'x-rapidapi-host': 'contextualwebsearch-websearch-v1.p.rapidapi.com',
            'x-rapidapi-key': os.environ.get("api_key")
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        response_data=json.loads(response.text)

        return response_data["value"]
    
    except BaseException as e:
        print(e)

def Home(request):
    
    company=request.GET.get('company')

    if company:
        news_list=NewsModel.objects.filter(dictionary_tokens=company)
    else:
        news_list=NewsModel.objects.all()

    
    return render(request,'home.html',context={'news_list':news_list})

def all_news(request):
    
    response_data=API_data()

    return render(request,'all_news.html',context={'articles':response_data})