from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import News

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context=context)

