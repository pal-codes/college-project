from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import News, Posts

# Create your views here.
def index(request):
    postlist = Posts.objects.all()
    context = { 'postlist' : postlist }
    return render(request, 'mainweb/index.html', context)

def about(request):
    return render(request, 'mainweb/abtus.html')

def news(request):
    newslist = News.objects.all()
    context = { 'newslist' : newslist }
    return render(request, 'mainweb/news.html', context)
    # return HttpResponse("{& for news in newslist &}  <h1>{{newslist.news}} </h1> {& endfor &}")

def contact(request):
    return render(request, 'mainweb/contact.html') 

def computer(request):
    return render(request, 'mainweb/comp.html')

def gymkhana(request):
    return render(request, 'mainweb/gymkhana.html')

def library(request):
    return render(request, 'mainweb/library.html')

def sports(request): 
    return render(request, 'mainweb/sports.html')