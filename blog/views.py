from django.shortcuts import render,get_object_or_404

from . models import Article

def home(request):
    post = Article.objects.filter(status="P").order_by('-publish')
    context={
        'post':post
    }
    return render(request,'blog/index.html',context)

def detail(request,blog_id):
    # detail =Article.objects.get(id=blog_id)
    detail = get_object_or_404(Article,id=blog_id,status="P")
    context={  
        'detail':detail
    }
    return render(request,'blog/post.html',context)
