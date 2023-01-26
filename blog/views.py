from django.views.generic import ListView,DetailView
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from . models import Article,Category


class ArticleListView(ListView):
    # model = Article
    # template_name = 'blog/index.html'
    # context_object_name= 'post'
    queryset = Article.objects.filter(status="P")
    paginate_by = 4


class ArticleDetailView(DetailView):
    def get_object(self):
        blog_id = self.kwargs.get('blog_id')
        return get_object_or_404(Article,id=blog_id,status="P")


class ArticleCategoryList(ListView):
    paginate_by = 4
    template_name = 'blog/category_list.html'
    
    def get_queryset(self):
        global category
        blog_id = self.kwargs.get('blog_id')
        category = get_object_or_404(Category.objects.active(),id=blog_id)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class ArticleAuthorList(ListView):
    paginate_by = 4
    template_name = 'blog/author_list.html'
    
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User,username = username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context





# def home(request):
#     articles_list = Article.objects.filter(status="P")
#     paginator = Paginator(articles_list,4)
#     page = request.GET.get('page',1)
#     post = paginator.get_page(page)

#     context= {
#         'post':post,
#     }
#     return render(request,'blog/index.html',context)


# def detail(request,blog_id):
#     # detail =Article.objects.get(id=blog_id)
#     detail = get_object_or_404(Article,id=blog_id,status="P")
#     context={  
#         'detail':detail
#     }
#     return render(request,'blog/post.html',context)

# def category(request,blog_id,page=1):
#     # cat =Category.objects.get(id=blog_id)
#     cat = get_object_or_404(Category,id=blog_id,status=True)    
#     articles_list = cat.articles.published()
#     paginator = Paginator(articles_list,4)
#     page = request.GET.get('page',1)
#     post = paginator.get_page(page)

#     context={  
#         'cat':cat,
#         'post':post
#     }
#     return render(request,'blog/category.html',context)
