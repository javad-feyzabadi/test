from django.urls import path
from . views import home,detail


urlpatterns=[
    path('',home,name='home'),
    path('detail/<int:blog_id>/',detail,name='detail'),

]