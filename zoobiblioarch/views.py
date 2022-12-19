from django.shortcuts import render
from .models import *
from django.http import JsonResponse

import json

# Create your views here.

def homepage(request):
    
 article_count= Article.objects.all().count()
 author_count= Author.objects.all().count()
 region_count= Region.objects.all().count()
 keywords_count= keyword.objects.all().count()

 context= {'article_count':  article_count,'author_count':author_count,'region_count':region_count,'keywords_count':keywords_count}
 
 return render(request, 'core/homepage.html',context)



 #TEAM HTML

def team(request):
    

   return render(request, 'core/team.html')
   

# list of articles 
def list_articles(request):
    article = Article.objects.all()
    context = {'article':article,}
    return render(request, 'core/list_of_articles.html', context)


# JSON
def json(request):
     
     rows = list(Article.objects.values())
     journals= list(Journal.objects.values())
     context = {'rows':rows,'journal':journals,}
     
     return JsonResponse(context, safe=False,)
# About
def about(request):
    

   return render(request, 'core/about.html')
   


