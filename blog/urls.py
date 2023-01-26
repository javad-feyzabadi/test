from django.urls import path
from . views import ( ArticleListView,ArticleDetailView,
                      ArticleCategoryList,ArticleAuthorList,

)

urlpatterns=[
    path('',ArticleListView.as_view(),name='home'),
    path('detail/<int:blog_id>/',ArticleDetailView.as_view(),name='detail'),
    path('category/<int:blog_id>/',ArticleCategoryList.as_view(),name='category'),
    path('author/<int:username>/',ArticleAuthorList.as_view(),name='author'),

]