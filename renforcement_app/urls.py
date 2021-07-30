from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',views.index, name="index"),
    path('years/<str:year>/', views.years, name='years')
]
