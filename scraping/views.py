import time
from django.shortcuts import render
from .models import StudentSearch
from .forms import  StudentGeneralSearch
from .scrap  import WebScraping , QuotesScraping
from django.http import HttpResponseRedirect, HttpResponse


def news(request):
    if request.method == 'POST':
        fm = StudentGeneralSearch(request.POST)
        if fm.is_valid():
            query=  fm.cleaned_data['query']
            if query=='news':
                return HttpResponseRedirect('/zeenews/')

            elif query=='quotes'or  query=='quote':
                return HttpResponseRedirect('/quotes/')
            else:
                return HttpResponse('Sorry Here You Search only News and Quotes')

    else:
        fm = StudentGeneralSearch()
        return render(request, 'scraping/home.html', {'form':fm})

def Zeenews(request):
    news = WebScraping()
    return render(request, 'scraping/news.html',{'news':news})


def Quotes(request):
    quotes  = QuotesScraping()
    return render(request, 'scraping/quotes.html', {'quotes':quotes})

