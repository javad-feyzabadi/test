from django.urls import path

from . views import ( ArticleListView,ArticleDetailView,
                      ArticleCategoryList,ArticleAuthorList,
                      ArticlePreView,

)

app_name = 'blog'


urlpatterns=[
    path('',ArticleListView.as_view(),name='home'),
    path('detail/<int:blog_id>/',ArticleDetailView.as_view(),name='detail'),
    path('category/<int:blog_id>/',ArticleCategoryList.as_view(),name='category'),
    path('preview/<int:pk>/',ArticlePreView.as_view(),name='preview'),


]