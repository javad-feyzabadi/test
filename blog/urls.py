from django.urls import path
from . views import ArticleListView,detail,category


urlpatterns=[
    path('',ArticleListView.as_view(),name='home'),
    path('detail/<int:blog_id>/',detail,name='detail'),
    path('category/<int:blog_id>/',category,name='category'),

]