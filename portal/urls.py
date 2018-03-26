from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('product_lamp', views.product_lamp),
    path('product_light', views.product_light),
    path('product_municipal', views.product_municipal),
    path('product_pip', views.product_pip),
    path('contact_us', views.contact_us),
    path('news_center', views.news_center),
    path('company', views.company),
    path('municipal', views.municipal),
    path(r'news_list/<str:news_date>', views.news_list),
]
