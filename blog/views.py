from django.views.generic import ListView,DetailView
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from . models import Article,Category

# def home(request):
#     articles_list = Article.objects.filter(status="P")
#     paginator = Paginator(articles_list,4)
#     page = request.GET.get('page',1)
#     post = paginator.get_page(page)

#     context= {
#         'post':post,
#     }
    # return render(request,'blog/index.html',context)

class ArticleListView(ListView):
    # model = Article
    # template_name = 'blog/index.html'
    # context_object_name= 'post'
    queryset = Article.objects.filter(status="P")
    paginate_by = 4


def detail(request,blog_id):
    # detail =Article.objects.get(id=blog_id)
    detail = get_object_or_404(Article,id=blog_id,status="P")
    context={  
        'detail':detail
    }
    return render(request,'blog/post.html',context)



def category(request,blog_id,page=1):
    # cat =Category.objects.get(id=blog_id)
    cat = get_object_or_404(Category,id=blog_id,status=True)    
    articles_list = cat.articles.published()
    paginator = Paginator(articles_list,4)
    page = request.GET.get('page',1)
    post = paginator.get_page(page)

    context={  
        'cat':cat,
        'post':post
    }
    return render(request,'blog/category.html',context)
