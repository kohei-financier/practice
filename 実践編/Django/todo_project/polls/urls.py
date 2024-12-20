from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('mypage/', views.mypage, name='mypage'),
    path('form/', views.form, name='form'),
    path('confirmform/', views.confirmform, name='confirmform'),
]
