from django.contrib import admin
from django.urls import path
from EventMan import views

urlpatterns =[
    path('',views.index,name='EventMan'),
    path('participation',views.ser,name='participation'),
    path('success',views.det,name='success'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('showevent',views.showevent,name='showevent'),
]