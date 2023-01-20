from django.urls import path
from . views import home,detail


urlpatterns=[
    path('',home,name='hello'),
    path('detail/<slug:slug>',detail,name='detail'),

]