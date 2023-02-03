from django.contrib.auth import views
from django.urls import path

from . views import (ArticleList,ArticleCreate,
                     ArticleUpdate,ArticleDelete,
                     Profile
)

app_name = 'accounts'

urlpatterns = [

    path("",ArticleList.as_view(),name='homee'),
    path("create/",ArticleCreate.as_view(),name='article-create'),
    path("update/<int:pk>",ArticleUpdate.as_view(),name='article-update'),
    path("delete/<int:pk>",ArticleDelete.as_view(),name='article-delete'),
    path("profile/",Profile.as_view(),name='profile'),

]


# urlpatterns += [
#     path('',ArticleList.as_view(),name='home'),
# ]