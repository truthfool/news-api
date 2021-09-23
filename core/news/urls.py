from django import urls
from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.Home,name='home'),
    path('all-news/',views.all_news,name='all_news'),
]