from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Article



class PostListView(ListView):
    queryset = Article.objects.filter(status="P")
    paginate_by = 10
    template_name = 'posts/posts.html'
    context_object_name = 'posts'