from django.urls import path
from .views import *

urlpatterns=[
    path('flash/1',first,name='main_url'),
    path('flash/2',second,name='second_url'),
    path('flash/3',tri,name='tri_url'),
    path('flash/4',four,name='four_url'),
]