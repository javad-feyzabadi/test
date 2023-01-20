from django.shortcuts import render

from . models import Article

def home(request):
    post = Article.objects.filter(status="P").order_by('-publish')
    context={
        'post':post
    }
    return render(request,'blog/home.html',context)

def detail(request,slug):
    detail = Article.objects.get(slug=slug)
    context={
        'detail':detail
    }
    return render(request,'blog/detail.html',context)
