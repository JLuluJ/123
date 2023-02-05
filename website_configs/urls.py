from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import TemplateView

urlpatterns = [
    # top keywords
    path('topword/', include('app_top_keyword.urls')),
    # top persons
    path('topperson/', include('app_top_person.urls')),
    # top name entity keyword
    path('topner/', include('app_top_ner.urls')),
    # user keyword analysis
    path('userkeyword/', include('app_user_keyword.urls')),
    # full text search and associated paragraphs for user keywords
    #path('userkeyword_assoc/', include('app_user_keyword_association.urls')),
    # user keyword sentiment analysis
    path('userkey_senti/', include('app_userkey_sentiment.urls')),

    # Sentiment analysis
    path('sentiment/', include('app_news_sentiment.urls')),

    # news classification
    path('news_cate/', include('app_news_classify.urls')),



]

