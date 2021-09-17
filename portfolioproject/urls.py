from django.contrib import admin
from django.urls import path
from portfolioproject import views
urlpatterns = [
             path('',views.home)
]
